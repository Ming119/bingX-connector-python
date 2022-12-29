'''
bingX.spot.market
'''

from bingX import ClientError

def symbols(self,
    symbol: str = None,
) -> dict:
    ''' Query Symbols
    GET /openApi/spot/v1/common/symbols

    https://bingx-api.github.io/docs/spot/market-interface.html#query-symbols
    '''
    res = self.get('/openApi/spot/v1/common/symbols', params={
        'symbol': symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def trades(self,
    symbol: str,
    limit:  int = None,
) -> dict:
    ''' Query transaction records
    GET /openApi/spot/v1/market/trades

    https://bingx-api.github.io/docs/spot/market-interface.html#query-transaction-records
    '''
    res = self.get('/openApi/spot/v1/market/trades', params={
        'symbol': symbol,
        'limit':  limit,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def depth(self,
    symbol: str,
    limit:  int = None,
) -> dict:
    ''' Query depth information
    GET /openApi/spot/v1/market/depth

    https://bingx-api.github.io/docs/spot/market-interface.html#query-depth-information
    '''
    res = self.get('/openApi/spot/v1/market/depth', params={
        'symbol': symbol,
        'limit':  limit,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']
