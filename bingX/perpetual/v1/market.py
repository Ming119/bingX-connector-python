'''
bingX.perpetual.v1.market
'''

from bingX import ClientError

def contracts(self) -> dict:
    ''' Contract Information
    GET /api/v1/market/getAllContracts

    https://bingx-api.github.io/docs/swap/market-api.html#_1-contract-information
    '''
    res = self.get("/api/v1/market/getAllContracts")

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def latest_price(self,
    symbol: str,
) -> dict:
    ''' Get Latest Price of a Trading Pair
    GET /api/v1/market/getLatestPrice

    https://bingx-api.github.io/docs/swap/market-api.html#_2-get-latest-price-of-a-trading-pair
    '''
    res = self.get("/api/v1/market/getLatestPrice", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def market_depth(self,
    symbol: str,
    level:  int = None,
) -> dict:
    ''' Get Market Depth
    GET /api/v1/market/getMarketDepth

    https://bingx-api.github.io/docs/swap/market-api.html#_3-get-market-depth
    '''
    res = self.get("/api/v1/market/getMarketDepth", params={
        "symbol": symbol,
        "level":  level,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def latest_trade(self,
    symbol: str,
) -> dict:
    ''' The latest Trade of a Trading Pair
    GET /api/v1/market/getMarketTrades

    https://bingx-api.github.io/docs/swap/market-api.html#_4-the-latest-trade-of-a-trading-pair
    '''
    res = self.get("/api/v1/market/getMarketTrades", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def current_funding_rate(self,
    symbol: str,
) -> dict:
    ''' Current Funding Rate
    GET /api/v1/market/getLatestFunding

    https://bingx-api.github.io/docs/swap/market-api.html#_5-current-funding-rate
    '''
    res = self.get("/api/v1/market/getLatestFunding", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def funding_rate_history(self,
    symbol: str,
) -> dict:
    ''' Funding Rate History
    GET /api/v1/market/getHistoryFunding

    https://bingx-api.github.io/docs/swap/market-api.html#_6-funding-rate-history
    '''
    res = self.get("/api/v1/market/getHistoryFunding", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def kline_data(self,
    symbol:    str,
    klineType: str,
) -> dict:
    ''' Get K-Line Data
    GET /api/v1/market/getLatestKline

    https://bingx-api.github.io/docs/swap/market-api.html#_7-get-k-line-data
    '''
    res = self.get("/api/v1/market/getLatestKline", params={
        "symbol":    symbol,
        "klineType": klineType,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def kline_data_history(self,
    symbol:    str,
    klineType: str,
    startTs:   int,
    endTs:     int,
) -> dict:
    ''' K-Line Data History
    GET /api/v1/market/getHistoryKlines

    https://bingx-api.github.io/docs/swap/market-api.html#_8-k-line-data-history
    '''
    res = self.get("/api/v1/market/getHistoryKlines", params={
        "symbol":    symbol,
        "klineType": klineType,
        "startTs":   startTs,
        "endTs":     endTs,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def open_positions(self,
    symbol: str,
) -> dict:
    ''' Get Swap Open Positions
    GET /api/v1/market/getOpenPositions

    https://bingx-api.github.io/docs/swap/market-api.html#_9-get-swap-open-positions
    '''
    res = self.get("/api/v1/market/getOpenPositions", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def ticker(self,
    symbol: str = None,
) -> dict:
    ''' Get Ticker
    GET /api/v1/market/getTicker

    https://bingx-api.github.io/docs/swap/market-api.html#_10-get-ticker
    '''
    res = self.get("/api/v1/market/getTicker", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']
