'''
bingX.spot.market
'''

def symbols(self, 
    symbol: str = None    
) -> dict:
    ''' Query Symbols
    GET /openApi/spot/v1/common/symbols

    https://bingx-api.github.io/docs/spot/market-interface.html#query-symbols
    '''
    return self.get('/openApi/spot/v1/common/symbols', params={
        'symbol': symbol
    })

def trades(self,
    symbol:     str,
    limit:      int   = None,
) -> dict:
    ''' Query Transaction Records
    GET /openApi/spot/v1/market/trades

    https://bingx-api.github.io/docs/spot/market-interface.html#query-transaction-records
    '''
    return self.get('/openApi/spot/v1/market/trades', params={
        'symbol':     symbol,
        'limit':      limit,
    })

def depth(self,
    symbol:     str,
    limit:      int   = None,
) -> dict:
    ''' Query Depth Information
    GET /openApi/spot/v1/market/depth

    https://bingx-api.github.io/docs/spot/market-interface.html#query-order-book
    '''
    return self.get('/openApi/spot/v1/market/depth', params={
        'symbol':     symbol,
        'limit':      limit,
    })