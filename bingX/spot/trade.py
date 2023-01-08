'''
bingX.spot.trade
'''

from bingX import ClientError

def place_order(self,
    symbol:        str,
    side:          str,
    type:          str,
    timeInForce:   str   = None,
    quantity:      float = None,
    quoteOrderQty: float = None,
    price:         float = None,
    recvWindow:    int   = None,
) -> dict:
    ''' Create an Order
    POST /openApi/spot/v1/trade/order

    https://bingx-api.github.io/docs/spot/trade-interface.html#create-an-order
    '''
    res = self.post('/openApi/spot/v1/trade/order', params={
        'symbol':        symbol,
        'side':          side,  
        'type':          type,
        'timeInForce':   timeInForce,
        'quantity':      quantity,
        'quoteOrderQty': quoteOrderQty,
        'price':         price,
        'recvWindow':    recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def cancel_order(self,
    symbol:     str,
    orderId:    int,
    recvWindow: int = None,
) -> dict:
    ''' Cancel an Order
    POST /openApi/spot/v1/trade/cancel

    https://bingx-api.github.io/docs/spot/trade-interface.html#cancel-an-order
    '''
    res = self.post('/openApi/spot/v1/trade/cancel', params={
        'symbol':     symbol,
        'orderId':    orderId,
        'recvWindow': recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def order(self,
    symbol:     str,
    orderId:    int,
    recvWindow: int = None,
) -> dict:
    ''' Query Orders
    GET /openApi/spot/v1/trade/query

    https://bingx-api.github.io/docs/spot/trade-interface.html#query-orders
    '''
    res = self.get('/openApi/spot/v1/trade/query', params={
        'symbol':     symbol,
        'orderId':    orderId,
        'recvWindow': recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def open_orders(self,   
    symbol:     str,
    recvWindow: int = None,
) -> dict:
    ''' Query Open Orders
    GET /openApi/spot/v1/trade/openOrders

    https://bingx-api.github.io/docs/spot/trade-interface.html#query-open-orders
    '''
    res = self.get('/openApi/spot/v1/trade/openOrders', params={
        'symbol':     symbol,
        'recvWindow': recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def order_history(self,
    symbol:     str,
    orderId:    int = None,
    startTime:  int = None,
    endTime:    int = None,
    pageIndex:  int = None,
    pageSize:   int = None,
    recvWindow: int = None,
) -> dict:
    ''' Query Order History
    GET /openApi/spot/v1/trade/historyOrders

    https://bingx-api.github.io/docs/spot/trade-interface.html#query-order-history
    '''
    res = self.get('/openApi/spot/v1/trade/historyOrders', params={
        'symbol':     symbol,
        'orderId':    orderId,
        'startTime':  startTime,
        'endTime':    endTime,
        'pageIndex':  pageIndex,
        'pageSize':   pageSize,
        'recvWindow': recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def assets(self,
    recvWindow: int = None,
) -> dict:
    ''' Query Assets
    GET /openApi/spot/v1/account/balance

    https://bingx-api.github.io/docs/spot/trade-interface.html#query-assets
    '''
    res = self.get('/openApi/spot/v1/account/balance', params={
        'recvWindow': recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']
