'''
bingX.perpetual.v1.other
'''

from bingX import ClientError

def generate_listen_key(self) -> dict:
    ''' Generate Listen Key
    POST /api/v1/user/auth/userDataStream

    https://bingx-api.github.io/docs/swap/other-interface.html#generate-listen-key
    '''
    res = self.post("/api/v1/user/auth/userDataStream")

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res

def extend_listen_key(self,
    listenKey: str,
) -> dict:
    ''' Extend Listen Key
    PUT /api/v1/user/auth/userDataStream

    https://bingx-api.github.io/docs/swap/other-interface.html#extend-listen-key-validity-period
    '''
    res = self.put("/api/v1/user/auth/userDataStream", params={
        "listenKey": listenKey,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res

def delete_listen_key(self,
    listenKey: str,
) -> dict:
    ''' Delete Listen Key
    DELETE /api/v1/user/auth/userDataStream

    https://bingx-api.github.io/docs/swap/other-interface.html#delete-listen-key
    '''
    res = self.delete("/api/v1/user/auth/userDataStream", params={
        "listenKey": listenKey,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res
