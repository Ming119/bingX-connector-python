'''
bingX.standard.trade
'''

from bingX import ClientError

def position(self) -> dict:
    ''' Position
    GET /openApi/contract/v1/allPosition

    https://bingx-api.github.io/docs/standard/contract-interface.html#position
    '''
    res = self.get("/openApi/contract/v1/allPosition")

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def order_history(self,
    symbol:    str,
    orderId:   int = None,
    startTime: int = None,
    endTime:   int = None,
    limit:     int = None,
) -> dict:
    ''' Historical order
    GET /openApi/contract/v1/allOrders

    https://bingx-api.github.io/docs/standard/contract-interface.html#historical-order
    '''
    res = self.get("/openApi/contract/v1/allOrders", params={
        "symbol":    symbol,
        "orderId":   orderId,
        "startTime": startTime,
        "endTime":   endTime,
        "limit":     limit,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def balance(self) -> dict:
    ''' Query standard contract balance
    GET /openApi/contract/v1/balance

    https://bingx-api.github.io/docs/standard/contract-interface.html#query-standard-contract-balance
    '''
    res = self.get("/openApi/contract/v1/balance")

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']
