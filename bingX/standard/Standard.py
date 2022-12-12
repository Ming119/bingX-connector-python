from bingX import API

class Standard(API):
    def __init__(self,
        api_key:    str,
        api_secret: str,
        base_url:   str = None
    ) -> object:
        super().__init__(
            api_key    = api_key,
            api_secret = api_secret,
            base_url   = base_url or "https://open-api.bingx.com",
            api_type   = "standard"
        )
    
    def position(self) -> dict:
        return self.get("/openApi/contract/v1/allPosition")
    
    def order_history(self,
        symbol:    str,
        orderId:   int = None,
        startTime: int = None,
        endTime:   int = None,
        limit:     int = None
    ) -> dict:
        return self.get("/openApi/contract/v1/allOrders", params={
            "symbol":    symbol,
            "orderId":   orderId,
            "startTime": startTime,
            "endTime":   endTime,
            "limit":     limit
        })