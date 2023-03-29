'''
bingX.perpetual.v1.trade
'''

from typing import List
from bingX import ClientError

def place_order(self,
    symbol:           str,
    side:             str,
    entrustPrice:     float,
    entrustVolume:    float,
    tradeType:        str,
    action:           str,
    takerProfitPrice: float = None,
    stopLossPrice:    float = None,
) -> dict:
    ''' Place a New Order
    POST /api/v1/user/trade

    https://bingx-api.github.io/docs/swap/trade-api.html#_1-place-a-new-order
    '''
    res = self.post("/api/v1/user/trade", params={
        "symbol":           symbol,
        "side":             side,
        "entrustPrice":     entrustPrice,
        "entrustVolume":    entrustVolume,
        "tradeType":        tradeType,
        "action":           action,
        "takerProfitPrice": takerProfitPrice,
        "stopLossPrice":    stopLossPrice,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def close_position(self,
    symbol:     str,
    positionId: str,
) -> dict:
    ''' One-Click Close Position
    POST /api/v1/user/oneClickClosePosition

    https://bingx-api.github.io/docs/swap/trade-api.html#_2-one-click-close-position
    '''
    res = self.post("/api/v1/user/oneClickClosePosition", params={
        "symbol":     symbol,
        "positionId": positionId,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def close_all_positions(self) -> dict:
    ''' One-Click Close All Positions
    POST /api/v1/user/oneClickCloseAllPositions

    https://bingx-api.github.io/docs/swap/trade-api.html#_3-one-click-close-all-positions
    '''
    res = self.post("/api/v1/user/oneClickCloseAllPositions")

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def cancel_order(self,
    symbol:  str,
    orderId: str,
) -> dict:
    ''' Cancel an Order
    https://bingx-api.github.io/docs/swap/trade-api.html#_4-cancel-an-order
    '''
    res = self.post("/api/v1/user/cancelOrder", params={
        "symbol":  symbol,
        "orderId": orderId,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def cancel_orders(self,
    symbol:   str,
    orderIds: List[str],
) -> dict:
    ''' Cancel Multiple Orders
    POST /api/v1/user/batchCancelOrders

    https://bingx-api.github.io/docs/swap/trade-api.html#_5-cancel-a-batch-of-orders
    '''
    res = self.post("/api/v1/user/batchCancelOrders", params={
        "symbol": symbol,
        "oids":   orderIds,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def cancel_all_orders(self) -> dict:
    ''' Cancel All Orders
    POST /api/v1/user/cancelAll

    https://bingx-api.github.io/docs/swap/trade-api.html#_6-cancel-all-orders
    '''
    res = self.post("/api/v1/user/cancelAll")

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def unfilled_order_acquisition(self,
    symbol: str,
) -> dict:
    ''' Unfilled Order Acquisition
    POST /api/v1/user/pendingOrders

    https://bingx-api.github.io/docs/swap/trade-api.html#_7-unfilled-order-acquisition
    '''
    res = self.post("/api/v1/user/pendingOrders", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def order_details(self,
    symbol:  str,
    orderId: str,
) -> dict:
    ''' Query Order Details
    POST /api/v1/user/orderInfo

    https://bingx-api.github.io/docs/swap/trade-api.html#_8-query-order-details
    '''
    res = self.post("/api/v1/user/orderInfo", params={
        "symbol":  symbol,
        "orderId": orderId,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def margin_mode(self,
    symbol: str,
) -> dict:
    ''' Query Margin Mode
    POST /api/v1/user/getMarginMode

    https://bingx-api.github.io/docs/swap/trade-api.html#_9-query-margin-mode
    '''
    res = self.post("/api/v1/user/getMarginMode", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def switch_margin_mode(self,
    symbol:     str,
    marginMode: str,
) -> dict:
    ''' Switch Margin Mode
    POST /api/v1/user/setMarginMode

    https://bingx-api.github.io/docs/swap/trade-api.html#_10-switch-margin-mode
    '''
    res = self.post("/api/v1/user/setMarginMode", params={
        "symbol":     symbol,
        "marginMode": marginMode,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def leverage(self,
    symbol: str,
) -> dict:
    ''' Query Leverage
    POST /api/v1/user/getLeverage

    https://bingx-api.github.io/docs/swap/trade-api.html#_11-query-leverage
    '''
    res = self.post("/api/v1/user/getLeverage", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def switch_leverage(self,
    symbol:   str,
    side:     str,
    leverage: int,
) -> dict:
    ''' Switch Leverage
    POST /api/v1/user/setLeverage

    https://bingx-api.github.io/docs/swap/trade-api.html#_12-switch-leverage
    '''
    res = self.post("/api/v1/user/setLeverage", params={
        "symbol":   symbol,
        "side":     side,
        "leverage": leverage,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res

def force_orders(self,
    symbol:        str,
    autoCloseType: str,
    lastOrderId:   int,
    length:        int,
) -> dict:
    ''' User Force Orders
    POST /api/v1/user/forceOrders

    https://bingx-api.github.io/docs/swap/trade-api.html#_13-user-s-force-orders
    '''
    res = self.post("/api/v1/user/forceOrders", params={
        "symbol":        symbol,
        "autoCloseType": autoCloseType,
        "lastOrderId":   lastOrderId,
        "length":        length,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def orders_history(self,
    symbol:      str,
    lastOrderId: int,
    length:      int,
) -> dict:
    ''' User History Orders
    POST /api/v1/user/historyOrders

    https://bingx-api.github.io/docs/swap/trade-api.html#_14-user-s-history-orders
    '''
    res = self.post("/api/v1/user/historyOrders", params={
        "symbol":      symbol,
        "lastOrderId": lastOrderId,
        "length":      length,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def place_a_stop_order(self,
    positionId:      str,
    entrustVolume:   float,
    orderId:         str   = None,
    stopLossPrice:   float = None,
    takeProfitPrice: float = None,
) -> dict:
    ''' Place a Stop Order
    POST /api/v1/user/stopOrder

    https://bingx-api.github.io/docs/swap/trade-api.html#_15-place-a-stop-order
    '''
    res = self.post("/api/v1/user/stopOrder", params={
        "positionId":      positionId,
        "orderId":         orderId,
        "stopLossPrice":   stopLossPrice,
        "takeProfitPrice": takeProfitPrice,
        "entrustVolume":   entrustVolume,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def cancel_stop_order(self,
    orderId: str,
) -> dict:
    ''' Cancel a Stop Order
    POST /api/v1/user/cancelStopOrder

    https://bingx-api.github.io/docs/swap/trade-api.html#_16-cancel-stop-order
    '''
    res = self.post("/api/v1/user/cancelStopOrder", params={
        "orderId": orderId,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def stop_orders(self,
    symbol: str,
) -> dict:
    ''' Query Stop Orders
    POST /api/v1/user/pendingStopOrders

    https://bingx-api.github.io/docs/swap/trade-api.html#_17-query-stop-orders
    '''
    res = self.post("/api/v1/user/pendingStopOrders", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def stop_orders_history(self,
    symbol:      str,
    lastOrderId: int,
    length:      int,
) -> dict:
    ''' Stop Orders History
    POST /api/v1/user/historyStopOrders

    https://bingx-api.github.io/docs/swap/trade-api.html#_18-query-history-stop-orders
    '''
    res = self.post("/api/v1/user/historyStopOrders", params={
        "symbol":      symbol,
        "lastOrderId": lastOrderId,
        "length":      length,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']
