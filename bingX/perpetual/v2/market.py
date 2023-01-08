'''
bingX.perpetual.v2.market
'''

from bingX import ClientError

def contracts(self) -> dict:
    ''' Contract Information
    GET /openApi/swap/v2/quote/contracts

    https://bingx-api.github.io/docs/swapV2/market-api.html#_1-contract-information
    '''
    res = self.get("/openApi/swap/v2/quote/contracts")

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def latest_price(self,
    symbol: str = None,
) -> dict:
    ''' Get Latest Price of a Trading Pair
    GET /openApi/swap/v2/quote/price

    https://bingx-api.github.io/docs/swapV2/market-api.html#_2-get-latest-price-of-a-trading-pair
    '''
    res = self.get("/openApi/swap/v2/quote/price", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def market_depth(self,
    symbol: str,
    limit:  int = None,
) -> dict:
    ''' Get Market Depth
    GET /openApi/swap/v2/quote/depth

    https://bingx-api.github.io/docs/swapV2/market-api.html#_3-get-market-depth
    '''
    res = self.get("/openApi/swap/v2/quote/depth", params={
        "symbol": symbol,
        "limit":  limit,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def latest_trade(self,
    symbol: str,
    limit:  int = None,
) -> dict:
    ''' The latest Trade of a Trading Pair
    GET /openApi/swap/v2/quote/trades

    https://bingx-api.github.io/docs/swapV2/market-api.html#_4-the-latest-trade-of-a-trading-pair
    '''
    res = self.get("/openApi/swap/v2/quote/trades", params={
        "symbol": symbol,
        "limit":  limit,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def current_funding_rate(self,
    symbol: str = None,
) -> dict:
    ''' Current Funding Rate
    GET /openApi/swap/v2/quote/premiumIndex

    https://bingx-api.github.io/docs/swapV2/market-api.html#_5-current-funding-rate
    '''
    res = self.get("/openApi/swap/v2/quote/premiumIndex", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def funding_rate_history(self,
    symbol:    str,
    startTime: int = None,
    endTime:   int = None,
    limit:     int = None,
) -> dict:
    ''' Funding Rate History
    GET /openApi/swap/v2/quote/fundingRate

    https://bingx-api.github.io/docs/swapV2/market-api.html#_6-funding-rate-history
    '''
    res = self.get("/openApi/swap/v2/quote/fundingRate", params={
        "symbol":    symbol,
        "startTime": startTime,
        "endTime":   endTime,
        "limit":     limit,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def kline(self,
    symbol:    str,
    interval:  str,
    startTime: int = None,
    endTime:   int = None,
    limit:     int = None,
) -> dict:
    ''' K-Line Data
    GET /openApi/swap/v2/quote/klines

    https://bingx-api.github.io/docs/swapV2/market-api.html#_7-k-line-data
    '''
    res = self.get("/openApi/swap/v2/quote/klines", params={
        "symbol":    symbol,
        "interval":  interval,
        "startTime": startTime,
        "endTime":   endTime,
        "limit":     limit,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def get_open_positions(self,
    symbol: str,
) -> dict:
    ''' Get Swap Open Positions
    GET /openApi/swap/v2/quote/openInterest

    https://bingx-api.github.io/docs/swapV2/market-api.html#_8-get-swap-open-positions
    '''
    res = self.get("/openApi/swap/v2/quote/openInterest", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def ticker(self,
    symbol: str = None,
) -> dict:
    ''' Get Ticker
    GET /openApi/swap/v2/quote/ticker

    https://bingx-api.github.io/docs/swapV2/market-api.html#_9-get-ticker
    '''
    res = self.get("/openApi/swap/v2/quote/ticker", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']
