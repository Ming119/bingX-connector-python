'''
bingX.perpetual.trade
'''

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
    return self.post("/api/v1/user/trade", params={
        "symbol":           symbol,
        "side":             side,
        "entrustPrice":     entrustPrice,
        "entrustVolume":    entrustVolume,
        "tradeType":        tradeType,
        "action":           action,
        "takerProfitPrice": takerProfitPrice,
        "stopLossPrice":    stopLossPrice,
    })

def close_position(self,
    symbol:     str,
    positionId: str,
) -> dict:
    ''' One-Click Close Position
    POST /api/v1/user/oneClickClosePosition

    https://bingx-api.github.io/docs/swap/trade-api.html#_2-one-click-close-position
    '''
    return self.post("/api/v1/user/oneClickClosePosition", params={
        "symbol":     symbol,
        "positionId": positionId,
    })

def close_all_positions(self) -> dict:
    ''' One-Click Close All Positions
    POST /api/v1/user/oneClickCloseAllPositions

    https://bingx-api.github.io/docs/swap/trade-api.html#_3-one-click-close-all-positions
    '''
    return self.post("/api/v1/user/oneClickCloseAllPositions")

def cancel_order(self,
    symbol:  str,
    orderId: str,
) -> dict:
    ''' Cancel an Order
    https://bingx-api.github.io/docs/swap/trade-api.html#_4-cancel-an-order
    '''
    return self.post("/api/v1/user/cancelOrder", params={
        "symbol":  symbol,
        "orderId": orderId,
    })

def cancel_orders(self,
    symbol:   str,
    orderIds: list[str],
) -> dict:
    ''' Cancel Multiple Orders
    POST /api/v1/user/batchCancelOrders

    https://bingx-api.github.io/docs/swap/trade-api.html#_5-cancel-a-batch-of-orders
    '''
    return self.post("/api/v1/user/batchCancelOrders", params={
        "symbol": symbol,
        "oids":   orderIds,
    })

def cancel_all_orders(self) -> dict:
    ''' Cancel All Orders
    POST /api/v1/user/cancelAll

    https://bingx-api.github.io/docs/swap/trade-api.html#_6-cancel-all-orders
    '''
    return self.post("/api/v1/user/cancelAll")

def unfilled_order_acquisition(self,
    symbol: str,
) -> dict:
    ''' Unfilled Order Acquisition
    POST /api/v1/user/pendingOrders

    https://bingx-api.github.io/docs/swap/trade-api.html#_7-unfilled-order-acquisition
    '''
    return self.post("/api/v1/user/pendingOrders", params={
        "symbol": symbol,
    })

def order_details(self,
    symbol:  str,
    orderId: str,
) -> dict:
    ''' Query Order Details
    POST /api/v1/user/orderInfo

    https://bingx-api.github.io/docs/swap/trade-api.html#_8-query-order-details
    '''
    return self.post("/api/v1/user/orderInfo", params={
        "symbol":  symbol,
        "orderId": orderId,
    })

def margin_mode(self,
    symbol: str,
) -> dict:
    ''' Query Margin Mode
    POST /api/v1/user/getMarginMode

    https://bingx-api.github.io/docs/swap/trade-api.html#_9-query-margin-mode
    '''
    return self.post("/api/v1/user/getMarginMode", params={
        "symbol": symbol,
    })

def switch_margin_mode(self,
    symbol:     str,
    marginMode: str,
) -> dict:
    ''' Switch Margin Mode
    POST /api/v1/user/setMarginMode

    https://bingx-api.github.io/docs/swap/trade-api.html#_10-switch-margin-mode
    '''
    return self.post("/api/v1/user/setMarginMode", params={
        "symbol":     symbol,
        "marginMode": marginMode,
    })

def leverage(self,
    symbol: str,
) -> dict:
    ''' Query Leverage
    POST /api/v1/user/getLeverage

    https://bingx-api.github.io/docs/swap/trade-api.html#_11-query-leverage
    '''
    return self.post("/api/v1/user/getLeverage", params={
        "symbol": symbol,
    })

def switch_leverage(self,
    symbol:   str,
    side:     str,
    leverage: int,
) -> dict:
    ''' Switch Leverage
    POST /api/v1/user/setLeverage

    https://bingx-api.github.io/docs/swap/trade-api.html#_12-switch-leverage
    '''
    return self.post("/api/v1/user/setLeverage", params={
        "symbol":   symbol,
        "side":     side,
        "leverage": leverage,
    })

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
    return self.post("/api/v1/user/forceOrders", params={
        "symbol":        symbol,
        "autoCloseType": autoCloseType,
        "lastOrderId":   lastOrderId,
        "length":        length,
    })

def orders_history(self,
    symbol:      str,
    lastOrderId: int,
    length:      int,
) -> dict:
    ''' User History Orders
    POST /api/v1/user/historyOrders

    https://bingx-api.github.io/docs/swap/trade-api.html#_14-user-s-history-orders
    '''
    return self.post("/api/v1/user/historyOrders", params={
        "symbol":      symbol,
        "lastOrderId": lastOrderId,
        "length":      length,
    })

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
    return self.post("/api/v1/user/stopOrder", params={
        "positionId":      positionId,
        "orderId":         orderId,
        "stopLossPrice":   stopLossPrice,
        "takeProfitPrice": takeProfitPrice,
        "entrustVolume":   entrustVolume,
    })

def cancel_stop_order(self,
    orderId: str,
) -> dict:
    ''' Cancel a Stop Order
    POST /api/v1/user/cancelStopOrder

    https://bingx-api.github.io/docs/swap/trade-api.html#_16-cancel-stop-order
    '''
    return self.post("/api/v1/user/cancelStopOrder", params={
        "orderId": orderId,
    })

def stop_orders(self,
    symbol: str,
) -> dict:
    ''' Query Stop Orders
    POST /api/v1/user/pendingStopOrders

    https://bingx-api.github.io/docs/swap/trade-api.html#_17-query-stop-orders
    '''
    return self.post("/api/v1/user/pendingStopOrders", params={
        "symbol": symbol,
    })

def stop_orders_history(self,
    symbol:      str,
    lastOrderId: int,
    length:      int,
) -> dict:
    ''' Stop Orders History
    POST /api/v1/user/historyStopOrders

    https://bingx-api.github.io/docs/swap/trade-api.html#_18-query-history-stop-orders
    '''
    return self.post("/api/v1/user/historyStopOrders", params={
        "symbol":      symbol,
        "lastOrderId": lastOrderId,
        "length":      length,
    })
