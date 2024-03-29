'''
bingX.perpetual.v2.trade
'''

from typing import List
from bingX import ClientError

def trade_order(self,
    symbol:       str,
    type:         str,
    side:         str,
    positionSide: str   = None,
    price:        float = None,
    quantity:     float = None,
    stopPrice:    float = None,
    recvWindow:   int   = None,
    reduceOnly:   bool = None,
) -> dict:
    ''' Place a New Order
    POST /openApi/swap/v2/trade/order

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_1-trade-order
    '''
    res = self.post("/openApi/swap/v2/trade/order", params={
        "symbol":       symbol,
        "type":         type,
        "side":         side,
        "positionSide": positionSide,
        "price":        price,
        "quantity":     quantity,
        "stopPrice":    stopPrice,
        "recvWindow":   recvWindow,
        "reduceOnly":   reduceOnly
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def trade_order_test(self,
    symbol:       str,
    type:         str,
    side:         str,
    positionSide: str   = None,
    price:        float = None,
    quantity:     float = None,
    stopPrice:    float = None,
    recvWindow:   int   = None,
    reduceOnly:   bool = None,
) -> dict:
    ''' Place a New Order
    POST /openApi/swap/v2/trade/order/test

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_1-trade-order
    '''
    res = self.post("/openApi/swap/v2/trade/order/test", params={
        "symbol":       symbol,
        "type":         type,
        "side":         side,
        "positionSide": positionSide,
        "price":        price,
        "quantity":     quantity,
        "stopPrice":    stopPrice,
        "recvWindow":   recvWindow,
        "reduceOnly":   reduceOnly
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def bulk_order(self,
    batchOrders: List,
    recvWindow:  int = None,
) -> dict:
    ''' Bulk order
    POST /openApi/swap/v2/trade/batchOrders

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_2-bulk-order
    '''
    res = self.post("/openApi/swap/v2/trade/batchOrders", params={
        "batchOrders": batchOrders,
        "recvWindow":  recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def close_all_positions(self,
    recvWindow: int = None,
) -> dict:
    ''' One-Click Close All Positions
    POST /openApi/swap/v2/trade/closeAllPositions

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_3-one-click-close-all-positions
    '''
    res = self.post("/openApi/swap/v2/trade/closeAllPositions", params={
        "recvWindow": recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def cancel_order(self,
    orderId:    int,
    symbol:     str,
    recvWindow: int = None,
) -> dict:
    ''' Cancel an Order
    DELETE /openApi/swap/v2/trade/order

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_4-cancel-an-order
    '''
    res = self.delete("/openApi/swap/v2/trade/order", params={
        "orderId":    orderId,
        "symbol":     symbol,
        "recvWindow": recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def cancel_orders(self,
    symbol:      str,
    orderIdList: List[int],
    recvWindow:  int = None,
) -> dict:
    ''' Cancel a Batch of Orders
    DELETE /openApi/swap/v2/trade/batchOrders

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_5-cancel-a-batch-of-orders
    '''
    res = self.delete("/openApi/swap/v2/trade/batchOrders", params={
        "symbol":      symbol,
        "orderIdList": orderIdList,
        "recvWindow":  recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def cancel_all_orders(self,
    symbol:     str,
    recvWindow: int = None,
) -> dict:
    ''' Cancel All Orders
    DELETE /openApi/swap/v2/trade/allOpenOrders

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_6-cancel-all-orders
    '''
    res = self.post("/openApi/swap/v2/trade/allOpenOrders", params={
        "symbol":     symbol,
        "recvWindow": recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def current_orders(self,
    symbol:     str,
    recvWindow: int = None,
) -> dict:
    ''' Query all current pending orders
    GET /openApi/swap/v2/trade/openOrders

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_7-query-all-current-pending-orders
    '''
    res = self.get("/openApi/swap/v2/trade/openOrders", params={
        "symbol":     symbol,
        "recvWindow": recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def order(self,
    symbol:     str,
    orderId:    int,
    recvWindow: int = None,
) -> dict:
    ''' Query Order
    GET /openApi/swap/v2/trade/order

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_8-query-order
    '''
    res = self.get("/openApi/swap/v2/trade/order", params={
        "symbol":     symbol,
        "orderId":    orderId,
        "recvWindow": recvWindow,
    })
    
    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def margin_mode(self,
    symbol:     str,
    recvWindow: int = None,
) -> dict:
    ''' Query Margin Mode
    GET /openApi/swap/v2/trade/marginType

    recvWindow
    '''
    res = self.get("/openApi/swap/v2/trade/marginType", params={
        "symbol":     symbol,
        "recvWindow": recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def switch_margin_mode(self,
    symbol:     str,
    marginType: str,
    recvWindow: int = None,
) -> dict:
    ''' Switch Margin Mode
    POST /openApi/swap/v2/trade/marginType

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_10-switch-margin-mode
    '''
    res = self.post("/openApi/swap/v2/trade/marginType", params={
        "symbol":     symbol,
        "marginType": marginType,
        "recvWindow": recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res  # No "data" return? 

def leverage(self,
    symbol:     str,
    recvWindow: int = None,
) -> dict:
    ''' Query Leverage
    GET /openApi/swap/v2/trade/leverage

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_11-query-leverage
    '''
    res = self.get("/openApi/swap/v2/trade/leverage", params={
        "symbol":     symbol,
        "recvWindow": recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def switch_leverage(self,
    symbol:     str,
    side:       str,
    leverage:   int,
    recvWindow: int = None,
) -> dict:
    ''' Switch Leverage
    POST /openApi/swap/v2/trade/leverage

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_12-switch-leverage
    '''
    res = self.post("/openApi/swap/v2/trade/leverage", params={
        "symbol":     symbol,
        "side":       side,
        "leverage":   leverage,
        "recvWindow": recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def force_orders(self,
    symbol:        str = None,
    autoCloseType: str = None,
    startTime:     int = None,
    endTime:       int = None,
    limit:         int = None,
    recvWindow:    int = None,
) -> dict:
    ''' User Force Orders
    GET /openApi/swap/v2/trade/forceOrders

    https://bingx-api.github.io/docs/swap/trade-api.html#_13-user-s-force-orders
    '''
    res = self.get("/openApi/swap/v2/trade/forceOrders", params={
        "symbol":        symbol,
        "autoCloseType": autoCloseType,
        "startTime":     startTime,
        "endTime":       endTime,
        "limit":         limit,
        "recvWindow":    recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def orders_history(self,
    symbol:     str,
    orderId:    int = None,
    startTime:  int = None,
    endTime:    int = None,
    limit:      int = 500,
    recvWindow: int = None,
) -> dict:
    ''' User History Orders
    GET /openApi/swap/v2/trade/allOrders

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_14-user-s-history-orders
    '''
    res = self.get("/openApi/swap/v2/trade/allOrders", params={
        "symbol":     symbol,
        "orderId":    orderId,
        "startTime":  startTime,
        "endTime":    endTime,
        "limit":      limit,
        "recvWindow": recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def adjust_isolated_margin(self,
    symbol:       str,
    amount:       float,
    type:         int,
    positionSide: str = None,
    recvWindow:   int = None,
) -> dict:
    ''' Adjust isolated margin
    POST /openApi/swap/v2/trade/positionMargin

    https://bingx-api.github.io/docs/swapV2/trade-api.html#_15-adjust-isolated-margin
    '''
    res = self.get("/openApi/swap/v2/trade/allOrders", params={
        "symbol":       symbol,
        "amount":       amount,
        "type":         type,
        "positionSide": positionSide,
        "recvWindow":   recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res  # no "data" return?