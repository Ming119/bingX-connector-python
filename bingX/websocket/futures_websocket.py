from bingX.websocket.websocket_client import BingxWebsocketClient


class UMFuturesWebsocketClient(BingxWebsocketClient):
    def __init__(
            self,
            stream_url="wss://open-api-swap.bingx.com/swap-market",
            on_message=None,
            on_open=None,
            on_close=None,
            on_error=None,
            listen_key=None
    ):
        if listen_key is not None:
            stream_url = stream_url + "?listenKey=" + listen_key
        print(stream_url)
        super().__init__(
            stream_url,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
        )

    def latest_mark_price(self, symbol: str, id=None, action=None, **kwargs):
        """Mark Price Streams

        Push latest mark price changes.

        Subscription Type
        dataType is <symbol>@markPrice, such as BTC-USDT@markPrice.

        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/market.html#Subscribe%20to%20latest%20mark%20price%20changes

        """
        stream_name = symbol + "@markPrice"

        self.send_message_to_server(stream_name, action=action, id=id)

    def last_price_changes(self, symbol: str, id=None, action=None, **kwargs):

        """
        Subscribe to latest price changes

        Push latest price changes.

        Subscription Type
        dataType is <symbol>@lastPrice, such as BTC-USDT@lastPrice.

        symbol:
            string
            There must be a hyphen/ "-" in the trading pair symbol. eg: BTC-USDT.

        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/market.html#Subscribe%20to%20latest%20price%20changes

        """
        stream_name = symbol + "@lastPrice"

        self.send_message_to_server(stream_name, action=action, id=id)

    def kline(self, symbol: str, interval: str, id=None, action=None, **kwargs):
        """Kline/Candlestick Streams

        Subscribe to market k-line data of one trading pair

        Subscription Type
        The dataType is <symbol>@kline_<interval> E.g. BTC-USDT@kline_1m

        Subscription Example
        {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType": "sub","dataType":"BTC-USDT@kline_1m"}

        For more about return error codes, please see the error code description on the homepage.


        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/market.html#Subscribe%20the%20Latest%20Trade%20Detail

        interval:
        m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

        - 1m
        - 3m
        - 5m
        - 15m
        - 30m
        - 1h
        - 2h
        - 4h
        - 6h
        - 8h
        - 12h
        - 1d
        - 3d
        - 1w
        - 1M
        """
        stream_name = symbol + "@kline_" + str(interval)
        self.send_message_to_server(stream_name, action=action, id=id)

    def user_data(self, listen_key: str, id=None, action=None, **kwargs):
        """
        Listen to user data by using the provided listenKey
        https://bingx-api.github.io/docs/#/en-us/swapV2/socket/account.html#Account%20balance%20and%20position%20update%20push
        """
        self.send_message_to_server(listen_key, action=action, id=id)
