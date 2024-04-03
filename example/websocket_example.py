import gzip
import io

from bingX.websocket.futures_websocket import UMFuturesWebsocketClient

def read_websocket_message(_, message):
    print(message)


future_websocket = UMFuturesWebsocketClient(on_message=read_websocket_message)

"""
Symbol must contain - between coin and pair, interval must be like exchange time frames (1m,5m,15m,30m,1h) id can 
be empty and generate random by library action can be sub or unsub default is sub for unsub you must set it to unsub 
all messages from websocket will be sent to your function witch here is read_websocket_message

future_websocket.kline(symbol="BTC-USDT", interval="1m",id="xxxxxxxxxxx",action="sub")
future_websocket.kline(symbol="BTC-USDT", interval="1m",id="xxxxxxxxxxx",action="unsub")

"""

future_websocket.kline(symbol="BTC-USDT", interval="1m")

"""
for using user_data to get position and order data you don't need to call any function the different is just when you 
initialized websocket class that here is UMFuturesWebsocketClient, for using user_data you need to create a listen_key
and sent it to the class.
just follow example
"""

user_data = UMFuturesWebsocketClient(on_message=read_websocket_message,listen_key="x")

"""
with this code you can receive user_data in read_websocket_message and do what ever you want to do.
just remember listen_key need to extend every 1 hour and websocket connection will be destroyed in 24 hours
for creating and expanding listen_key you can use :
from bingX.perpetual.v2 import other

listen_key = other.generate_listen_key('API_KEY')
other.delete_listen_key('listen_key')
other.extend_listen_key('listen_key')

"""

