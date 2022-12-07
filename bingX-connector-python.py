import urllib.request
import hmac
from time import time
from enum import Enum

class RestAPI:
    def __init__(self, baseUrl:str, apiKey:str, secret:str):
        self.baseUrl = baseUrl
        self.secret = secret
        self.headers = {
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-BX-APIKEY': apiKey
        }
    
    def _handleParams(self, params):
        if params is None: params = {}
        params['timestamp'] = round(time() * 1000)
        params = '&'.join(f'{k}={v}' for k,v in params.items() if v is not None)
        params += f'&signature={self._signature(params)}'
        return params

    def _signature(self, params:str):
        return hmac.new(self.secret.encode(), params.encode(), 'sha256').hexdigest()

    def get(self, endpoint:str, params:dict=None):
        params = self._handleParams(params)
        req = urllib.request.Request(f'{self.baseUrl}{endpoint}?{params}', headers=self.headers, method='GET')
        return urllib.request.urlopen(req).read().decode()

    def post(self, endpoint:str, params:dict=None):
        params = self._handleParams(params)
        req = urllib.request.Request(f'{self.baseUrl}{endpoint}?{params}', headers=self.headers, method='POST')
        return urllib.request.urlopen(req).read().decode()

    def put(self, endpoint:str, params:dict=None):
        params = self._handleParams(params)
        req = urllib.request.Request(f'{self.baseUrl}{endpoint}?{params}', headers=self.headers, method='PUT')
        return urllib.request.urlopen(req).read().decode()

    def delete(self, endpoint:str, params:dict=None):
        params = self._handleParams(params)
        req = urllib.request.Request(f'{self.baseUrl}{endpoint}?{params}', headers=self.headers, method='DELETE')
        return urllib.request.urlopen(req).read().decode()   

class StandContractClient(RestAPI):
    def __init__(self, apiKey:str, secret:str, baseUrl:str='https://open-api.bingx.com'):
        super().__init__(baseUrl, apiKey, secret)
    
    # ========== TRADE INTERFACE ===============================================
    def position(self):
        return self.get(f'/openApi/contract/v1/allPosition')
    
    def orderHistory(self, symbol:str, orderId:int=None, startTime:int=None, endTime:int=None, limit:int=None):
        return self.get(f'/openApi/contract/v1/allOrders', params={
            'symbol':    symbol,
            'orderId':   orderId,
            'startTime': startTime,
            'endTime':   endTime,
            'limit':     limit
        })
    
    # ==========================================================================

# ==============================================================================

class SpotClient(RestAPI):
    def __init__(self, apiKey:str, secret:str, baseUrl:str='https://open-api.bingx.com'):
        super().__init__(baseUrl, apiKey, secret)

    # ========== TRADE INTERFACE ===============================================
    def placeOrder(self, symbol:str, side:str, type:str, timeInForce:str=None, quantity:float=None, quoteOrderQty:float=None, price:float=None, recvWindow:int=None):
        return self.post('/spot/v1/trade/order', params={
            'symbol':        symbol,
            'side':          side,
            'type':          type,
            'timeInForce':   timeInForce,
            'quantity':      quantity,
            'quoteOrderQty': quoteOrderQty,
            'price':         price,
            'recvWindow':    recvWindow,
        })
    
    def cancelOrder(self, symbol:str, orderId:int, recvWindow:int=None):
        return self.post('/openApi/spot/v1/trade/cancel', params={
            'symbol':     symbol,
            'orderId':    orderId,
            'recvWindow': recvWindow,
        })

    def orders(self, symbol:str, orderId:int, recvWindow:int=None):
        return self.get('/openApi/spot/v1/trade/query', params={
            'symbol':     symbol,
            'orderId':    orderId,
            'recvWindow': recvWindow,
        })
    
    def openOrders(self, symbol:str, recvWindow:int=None):
        return self.get('/openApi/spot/v1/trade/openOrders', params={
            'symbol':     symbol,
            'recvWindow': recvWindow,
        })
    
    def orderHistory(self, symbol:str, orderId:int=None, startTime:int=None, endTime:int=None, pageIndex:int=None, pageSize:int=None, recvWindow:int=None):
        return self.get('/openApi/spot/v1/trade/orderHistory', params={
            'symbol':     symbol,
            'orderId':    orderId,
            'startTime':  startTime,
            'endTime':    endTime,
            'pageIndex':  pageIndex,
            'pageSize':   pageSize,
            'recvWindow': recvWindow,
        })

    def balance(self, timestamp:int=None):
        return self.get('/openApi/spot/v1/account/balance', params={
            'timestamp': timestamp,
        })
    
    # ==========================================================================

    # ========== MARKET INTERFACE ==============================================
    def symbols(self, symbol:str=None):
        return self.get('/openApi/spot/v1/common/symbols', params={
            'symbol': symbol,
        })
    
    def transactionRecords(self, symbol:str, limit:int=None):
        return self.get('/openApi/spot/v1/market/trades', params={
            'symbol': symbol,
            'limit':  limit,
        })
    
    def depth(self, symbol:str, limit:int=None):
        return self.get('/openApi/spot/v1/market/depth', params={
            'symbol': symbol,
            'limit':  limit,
        })

    # ==========================================================================

    # ========== USER UNIVERSAL TRANSFER INTERFACE =============================
    class TransferType(Enum):
        FUND_SFUTURES     = 'FUND_SFUTURES'
        SFUTURES_FUND     = 'SFUTURES_FUND'
        FUND_PFUTURES     = 'FUND_PFUTURES'
        PFUTURES_FUND     = 'PFUTURES_FUND'
        SFUTURES_PFUTURES = 'SFUTURES_PFUTURES'
        PFUTURES_SFUTURES = 'PFUTURES_SFUTURES'

    def userUniversalTransfer(self, type:TransferType, asset:str=None, amount:int=None, recvWindow:int=None):
        return self.post('/openApi/api/v3/asset/transfer', params={
            'type':       type,
            'asset':      asset,
            'amount':     amount,
            'recvWindow': recvWindow,
        })
    
    def userUniversalTransferHistory(self, type:TransferType, startTime:int=None, endTime:int=None, current:int=None, size:int=None, recvWindow:int=None):
        return self.get('/openApi/api/v3/asset/transfer', params={
            'type':       type,
            'startTime':  startTime,
            'endTime':    endTime,
            'current':    current,
            'size':       size,
            'recvWindow': recvWindow,
        })
    
    def depositHistory(self, coin:str=None, status:int=None, startTime:int=None, endTime:int=None, offset:int=None, limit:int=None, recvWindow:int=None):
        return self.get('/openApi/api/v3/capital/deposit/hisrec', params={
            'coin':       coin,
            'status':     status,
            'startTime':  startTime,
            'endTime':    endTime,
            'offset':     offset,
            'limit':      limit,
            'recvWindow': recvWindow,
        })
    
    def withdrawHistory(self, coin:str=None, withdrawOrderId:str=None, status:int=None, startTime:int=None, endTime:int=None, offset:int=None, limit:int=None, recvWindow:int=None):
        return self.get('/openApi/api/v3/capital/withdraw/history', params={
            'coin':            coin,
            'withdrawOrderId': withdrawOrderId,
            'status':          status,
            'startTime':       startTime,
            'endTime':         endTime,
            'offset':          offset,
            'limit':           limit,
            'recvWindow':      recvWindow,
        })

    # ==========================================================================

# ==============================================================================