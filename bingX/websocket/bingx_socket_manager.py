import gzip
import io

import logging
import threading
from websocket import (
    ABNF,
    create_connection,
    WebSocketException,
    WebSocketConnectionClosedException,
)


class BinanceSocketManager(threading.Thread):
    def __init__(
            self,
            stream_url,
            on_message=None,
            on_open=None,
            on_close=None,
            on_error=None,
            logger=None,
    ):
        threading.Thread.__init__(self)
        if not logger:
            logger = logging.getLogger(__name__)
        self.logger = logger
        self.stream_url = stream_url
        self.on_message = on_message
        self.on_open = on_open
        self.on_close = on_close

        self.on_error = on_error

        self.create_ws_connection()

    def create_ws_connection(self):
        self.logger.error(
            f"Creating connection with WebSocket Server: {self.stream_url}",
        )
        self.ws = create_connection(self.stream_url)
        self.logger.error(
            f"WebSocket connection has been established: {self.stream_url}",
        )
        self._callback(self.on_open)

    def run(self):
        self.read_data()

    def send_message(self, message):
        self.logger.error("Sending message to BingX WebSocket Server: %s", message)
        self.ws.send(message)

    def read_data(self):
        data = ""
        while True:
            try:
                op_code, frame = self.ws.recv_data_frame(True)
            except WebSocketException as e:
                if isinstance(e, WebSocketConnectionClosedException):
                    self.logger.error("Lost websocket connection")
                    print(str(e))
                else:
                    self.logger.error("Websocket exception: {}".format(e))
                raise e
            except Exception as e:
                self.logger.error("Exception in read_data: {}".format(e))
                raise e

            if op_code == ABNF.OPCODE_CLOSE:
                self.logger.warning(
                    "CLOSE frame received, closing websocket connection"
                )
                self._callback(self.on_close)
                break
            else:
                data = frame.data
                if op_code == ABNF.OPCODE_TEXT:
                    data = data.decode("utf-8")

                compressed_data = gzip.GzipFile(fileobj=io.BytesIO(data), mode='rb')
                decompressed_data = compressed_data.read()
                utf8_data = decompressed_data.decode('utf-8')
                if utf8_data == "Ping":
                    self.ws.send("Pong")
                else:
                    self._callback(self.on_message, utf8_data)

    def close(self):
        if not self.ws.connected:
            self.logger.warn("Websocket already closed")
        else:
            self.ws.send_close()
        return

    def _callback(self, callback, *args):
        if callback:
            try:
                callback(self, *args)
            except Exception as e:
                self.logger.error("Error from callback {}: {}".format(callback, e))
                if self.on_error:
                    self.on_error(self, e)
