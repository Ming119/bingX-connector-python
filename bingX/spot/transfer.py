'''
bingX.spot.transfer
'''

def transfer(self, 
    type:       str,
    asset:      str   = None,
    amount:     float = None,
    recvWindow: int   = None
) -> dict:
    ''' User Universal Transfer
    POST /openApi/api/v3/asset/transfer

    https://bingx-api.github.io/docs/spot/user-interface.html#user-universal-transfer
    '''
    return self.post('/openApi/api/v3/asset/transfer', params={
        'type':       type,
        'asset':      asset,
        'amount':     amount,
        'recvWindow': recvWindow
    })

def transfer_history(self,
    type:       str,
    startTime:  int   = None,
    endTime:    int   = None,
    current:    int   = None,
    size:       int   = None,
    recvWindow: int   = None
) -> dict:
    ''' Query User Universal Transfer History (USER_DATA)
    GET /openApi/api/v3/asset/transfer

    https://bingx-api.github.io/docs/spot/user-interface.html#query-user-universal-transfer-history-user-data
    '''
    return self.get('/openApi/api/v3/asset/transfer', params={
        'type':       type,
        'startTime':  startTime,
        'endTime':    endTime,
        'current':    current,
        'size':       size,
        'recvWindow': recvWindow
    })

def deposit_history(self,
    coin:       str = None,
    status:     int = None,
    startTime:  int = None,
    endTime:    int = None,
    offset:     int = None,
    limit:      int = None,
    recvWindow: int = None
) -> dict:
    ''' Query Deposit History (USER_DATA)
    GET /openApi/api/v3/capital/deposit/hisrec

    https://bingx-api.github.io/docs/spot/user-interface.html#query-deposit-history-user-data
    '''
    return self.get('/openApi/api/v3/capital/deposit/hisrec', params={
        'coin':       coin,
        'status':     status,
        'startTime':  startTime,
        'endTime':    endTime,
        'offset':     offset,
        'limit':      limit,
        'recvWindow': recvWindow
    })

def withdraw_history(self,
    coin:            str = None,
    withdrawOrderId: str = None,
    status:          int = None,
    startTime:       int = None,
    endTime:         int = None,
    offset:          int = None,
    limit:           int = None,
    recvWindow:      int = None
) -> dict:
    ''' Query Withdraw History (USER_DATA)
    GET /openApi/api/v3/capital/withdraw/history

    https://bingx-api.github.io/docs/spot/user-interface.html#query-withdraw-history-user-data
    '''
    return self.get('/openApi/api/v3/capital/withdraw/history', params={
        'coin':            coin,
        'withdrawOrderId': withdrawOrderId,
        'status':          status,
        'startTime':       startTime,
        'endTime':         endTime,
        'offset':          offset,
        'limit':           limit,
        'recvWindow':      recvWindow
    })