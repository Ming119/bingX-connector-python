'''
bingX.standard.trade
'''

def position(self) -> dict:
    '''
    Position
    https://bingx-api.github.io/docs/standard/trade-interface.html#position

    :parameters:
        none
    
    :respone:
    |- parameter name   -|- type -|- description                                      -|
    |====================|========|====================================================|
    |  symbol            |  str   |  symbol                                            |
    |  initialMargin     |  num   |  margin                                            |
    |  leverage          |  num   |  leverage number                                   |
    |  unrealizedProfit  |  num   |  position unrealized profit and loss               |
    |  isolated          |  bool  |  whether it is isolated mode                       |
    |  entryPrice        |  num   |  holding cost price                                |
    |  positionSide      |  num   |  position direction, LONG and SHORT                |
    |  positionAmt       |  num   |  transaction data                                  |
    |  currentPrice      |  num   |  the current price. if there is no closing price,  |
    |                    |        |    the current price will be returned              |
    |  time              |  int   |  position opening time                             |
    '''
    return self.get("/openApi/contract/v1/allPosition")
    
def order_history(self,
    symbol:    str,
    orderId:   int = None,
    startTime: int = None,
    endTime:   int = None,
    limit:     int = None
) -> dict:
    '''
    Order History
    https://bingx-api.github.io/docs/standard/trade-interface.html#order-history

    :parameters:
    |- parameter name -|- type -|- description                                              -|
    |==================|========|============================================================|
    |  symbol          |  str   |  currency pair, the format is similar: BTC-USDT, required  |
    |  orderId         |  int   |  order id, optional                                        |
    |  startTime       |  int   |  start time, optional                                      |
    |  endTime         |  int   |  end time, optional                                        |
    |  limit           |  int   |  quantity, optional                                        |

    :respone:
    |- parameter name -|- type -|- description                                    -|
    |==================|========|==================================================|
    |  avgPrice        |  num   |  closeing price                                  |
    |  cumQuote        |  num   |  transaction amount                              |
    |  executedQty     |  num   |  volume                                          |
    |  orderId         |  num   |  system order number                             |
    |  positionSide    |  str   |  position direction, LONG and SHORT              |
    |  status          |  str   |  order status CLOSED                             |
    |  symbol          |  str   |  currency pair, the format is similar: BTC-USDT  |
    |  time            |  int   |  order time                                      |
    |  updateTime      |  int   |  update time                                     |
    |  margin          |  num   |  margin                                          |
    |  leverage        |  num   |  leverage number                                 |
    |  isolated        |  bool  |  whether it is isolated mode                     |
    |  closePrice      |  num   |  closeing price                                  |
    |  positionId      |  int   |  position ID                                     |
    '''
    return self.get("/openApi/contract/v1/allOrders", params={
        "symbol":    symbol,
        "orderId":   orderId,
        "startTime": startTime,
        "endTime":   endTime,
        "limit":     limit
    })