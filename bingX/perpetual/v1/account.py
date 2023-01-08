'''
bingX.perpetual.v1.account
'''

from bingX import ClientError

def balance(self,
    currency: str,
) -> dict:
    ''' Get Perpetual Swap Account Asset Information
    POST /api/v1/user/getBalance

    https://bingx-api.github.io/docs/swap/account-api.html#_1-get-perpetual-swap-account-asset-information
    '''
    res = self.post("/api/v1/user/getBalance", params={
        "currency": currency,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def positions(self,
    symbol: str,
) -> dict:
    ''' Perpetual Swap Positions
    POST /api/v1/user/getPositions

    https://bingx-api.github.io/docs/swap/account-api.html#_2-perpetual-swap-positions
    '''
    res = self.post("/api/v1/user/getPositions", params={
        "symbol": symbol,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']
