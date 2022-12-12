from  bingX import API

class Spot(API):
    def __init__(self,
        api_key:    str,
        api_secret: str,
        base_url:   str = None
    ) -> object:
        super().__init__(
            api_key    = api_key,
            api_secret = api_secret,
            base_url   = base_url or 'https://open-api.bingx.com',
            api_type   = 'spot'
        )
    
    def place_order(self,
        symbol:        str,
        side:          str,
        type:          str,
        timeInForce:   str   = None,
        quantity:      float = None,
        quoteOrderQty: float = None,
        price:         float = None,
        recvWindow:    int   = None
    ) -> dict:
        return self.post('/openApi/spot/v1/trade/order', params={
            'symbol':        symbol,
            'side':          side,  
            'type':          type,
            'timeInForce':   timeInForce,
            'quantity':      quantity,
            'quoteOrderQty': quoteOrderQty,
            'price':         price,
            'recvWindow':    recvWindow
        })
    
    def cancel_order(self,
        symbol:     str,
        orderId:    int,
        recvWindow: int = None
    ) -> dict:
        return self.post('/openApi/spot/v1/trade/cancel', params={
            'symbol':     symbol,
            'orderId':    orderId,
            'recvWindow': recvWindow
        })
    
    def order(self,
        symbol:     str,
        orderId:    int,
        recvWindow: int = None
    ) -> dict:
        return self.get('/openApi/spot/v1/trade/query', params={
            'symbol':     symbol,
            'orderId':    orderId,
            'recvWindow': recvWindow
        })
    
    def open_orders(self,   
        symbol:     str,
        recvWindow: int = None
    ) -> dict:
        return self.get('/openApi/spot/v1/trade/openOrders', params={
            'symbol':     symbol,
            'recvWindow': recvWindow
        })
    
    def order_history(self,
        symbol:     str,
        orderId:    int,
        startTime:  int = None,
        endTime:    int = None,
        pageIndex:  int = None,
        pageSize:   int = None,
        recvWindow: int = None
    ) -> dict:
        return self.get('/openApi/spot/v1/trade/allOrders', params={
            'symbol':     symbol,
            'orderId':    orderId,
            'startTime':  startTime,
            'endTime':    endTime,
            'pageIndex':  pageIndex,
            'pageSize':   pageSize,
            'recvWindow': recvWindow
        })
    
    def balance(self,
        recvWindow: int = None
    ) -> dict:
        return self.get('/openApi/spot/v1/account/balance', params={
            'recvWindow': recvWindow
        })
