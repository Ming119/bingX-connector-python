import _thread
import json
import random

import websocket
import gzip
import io


class Websocket(object):

    def __init__(self, URL='wss://open-api-swap.bingx.com/swap-market'):
        self.sub_link = None
        self.url = URL
        self.ws = None

    def on_open(self, ws):
        subStr = json.dumps(self.sub_link)
        ws.send(subStr)
        return "Subscribed to :" + subStr

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        if utf8_data == "Ping":
            ws.send("Pong")
        return utf8_data

    def on_error(self, ws, error):
        return error

    def on_close(self, ws, close_status_code, close_msg):
        return 'The connection is closed!'

    def user_data(self, listen_key):
        '''
        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/account.html#listenKey%20expired%20push
        '''
        self.url = self.url + '?listenKey=' + listen_key
        self.start()

    def kline(self, type, pair, time):
        self.sub_link = {"id": ''.join(random.choice(string.ascii_letters) for _ in range(10)), "reqType": type,
                         "dataType": pair + "@kline_" + time}
        self.start()
        ''''
        Get Price Kline With Websocket
        type can be sub or unsub
        time must be same as exchange time format like 1m,5m,15m,30m,1h
        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/market.html#Subscribe%20K-Line%20Data
        test.kline("sub","BTC-USDT","1m")
        '''

    def last_price(self, type, pair):
        self.sub_link = {"id": ''.join(random.choice(string.ascii_letters) for _ in range(10)), "reqType": type,
                         "dataType": pair + "@lastPrice"}
        self.start()

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()
