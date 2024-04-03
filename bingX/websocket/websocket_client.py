import json
import logging
import uuid

from bingX.websocket.bingx_socket_manager import BinanceSocketManager


def get_random_id():
    return str(uuid.uuid4())


class BingxWebsocketClient:
    ACTION_SUBSCRIBE = "sub"
    ACTION_UNSUBSCRIBE = "unsub"

    def __init__(
            self,
            stream_url,
            on_message=None,
            on_open=None,
            on_close=None,
            on_error=None,
            logger=None,
    ):
        if not logger:
            logger = logging.getLogger(__name__)
        self.logger = logger
        self.socket_manager = self._initialize_socket(
            stream_url,
            on_message,
            on_open,
            on_close,
            on_error,
            logger,
        )

        # start the thread
        self.socket_manager.start()
        self.logger.debug("BingX WebSocket Client started.")

    def _initialize_socket(
            self,
            stream_url,
            on_message,
            on_open,
            on_close,
            on_error,
            logger,
    ):
        return BinanceSocketManager(
            stream_url,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            logger=logger,
        )

    def _single_stream(self, stream):
        if isinstance(stream, str):
            return True
        elif isinstance(stream, list):
            return False
        else:
            raise ValueError("Invalid stream name, expect string or array")

    def send(self, message: dict):
        self.socket_manager.send_message(json.dumps(message))

    def send_message_to_server(self, message, action=None, id=None):
        if not id:
            id = get_random_id()
        if action != self.ACTION_UNSUBSCRIBE:
            return self.subscribe(message, id=id)
        return self.unsubscribe(message, id=id)

    def subscribe(self, stream, id=None):
        if not id:
            id = get_random_id()
        json_msg = json.dumps({"id": id, "reqType": "sub", "dataType": stream})
        print(json_msg)
        self.socket_manager.send_message(json_msg)

    def unsubscribe(self, stream, id=None):
        if not id:
            id = get_random_id()
        json_msg = json.dumps({"id": id, "reqType": "unsub", "dataType": stream})
        self.socket_manager.send_message(json_msg)

    def stop(self, id=None):
        self.socket_manager.close()
        self.socket_manager.join()
