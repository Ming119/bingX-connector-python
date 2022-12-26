'''
bingX.perpetual.market
'''

def contracts(self) -> dict:
    ''' Contract Information
    GET /api/v1/market/getAllContracts

    https://bingx-api.github.io/docs/swap/market-api.html#_1-contract-information
    '''
    return self.get("/api/v1/market/getAllContracts")

def latest_price(self,
    symbol: str,
) -> dict:
    ''' Get Latest Price of a Trading Pair
    GET /api/v1/market/getLatestPrice

    https://bingx-api.github.io/docs/swap/market-api.html#_2-get-latest-price-of-a-trading-pair
    '''
    return self.get("/api/v1/market/getLatestPrice", params={
        "symbol": symbol,
    })

def market_depth(self,
    symbol: str,
    level:  int = None,
) -> dict:
    ''' Get Market Depth
    GET /api/v1/market/getMarketDepth

    https://bingx-api.github.io/docs/swap/market-api.html#_3-get-market-depth
    '''
    return self.get("/api/v1/market/getMarketDepth", params={
        "symbol": symbol,
        "level":  level,
    })

def latest_trade(self,
    symbol: str,
) -> dict:
    ''' The latest Trade of a Trading Pair
    GET /api/v1/market/getMarketTrades

    https://bingx-api.github.io/docs/swap/market-api.html#_4-the-latest-trade-of-a-trading-pair
    '''
    return self.get("/api/v1/market/getMarketTrades", params={
        "symbol": symbol,
    })

def current_funding_rate(self,
    symbol: str,
) -> dict:
    ''' Current Funding Rate
    GET /api/v1/market/getLatestFunding

    https://bingx-api.github.io/docs/swap/market-api.html#_5-current-funding-rate
    '''
    return self.get("/api/v1/market/getLatestFunding", params={
        "symbol": symbol,
    })

def funding_rate_history(self,
    symbol: str,
) -> dict:
    ''' Funding Rate History
    GET /api/v1/market/getHistoryFunding

    https://bingx-api.github.io/docs/swap/market-api.html#_6-funding-rate-history
    '''
    return self.get("/api/v1/market/getHistoryFunding", params={
        "symbol": symbol,
    })

def kline_data(self,
    symbol:    str,
    klineType: str,
) -> dict:
    ''' Get K-Line Data
    GET /api/v1/market/getLatestKline

    https://bingx-api.github.io/docs/swap/market-api.html#_7-get-k-line-data
    '''
    return self.get("/api/v1/market/getLatestKline", params={
        "symbol":    symbol,
        "klineType": klineType,
    })

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
    return self.get("/api/v1/market/getHistoryKlines", params={
        "symbol":    symbol,
        "klineType": klineType,
        "startTs":   startTs,
        "endTs":     endTs,
    })

def open_positions(self,
    symbol: str,
) -> dict:
    ''' Get Swap Open Positions
    GET /api/v1/market/getOpenPositions

    https://bingx-api.github.io/docs/swap/market-api.html#_9-get-swap-open-positions
    '''
    return self.get("/api/v1/market/getOpenPositions", params={
        "symbol": symbol,
    })

def ticker(self,
    symbol: str = None,
) -> dict:
    ''' Get Ticker
    GET /api/v1/market/getTicker

    https://bingx-api.github.io/docs/swap/market-api.html#_10-get-ticker
    '''
    return self.get("/api/v1/market/getTicker", params={
        "symbol": symbol,
    })
