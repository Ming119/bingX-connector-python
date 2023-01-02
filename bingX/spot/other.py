'''
bingX.spot.other
'''

from bingX import ClientError

def generate_listen_key(self):
    ''' Generate Listen Key
    POST /openApi/user/auth/userDataStream

    https://bingx-api.github.io/docs/spot/other-interface.html#generate-listen-key
    '''
    res = self.post('/openApi/user/auth/userDataStream')

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res

def extend_listen_key(self,
    listenKey: str,
) -> None:
    ''' Extend Listen Key Validity period
    PUT /openApi/user/auth/userDataStream

    https://bingx-api.github.io/docs/spot/other-interface.html#extend-listen-key-validity-period
    '''
    res = self.put('/openApi/user/auth/userDataStream', params={
        'listenKey': listenKey,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res

def delete_listen_key(self,
    listenKey: str,
) -> None:
    ''' Delete Listen Key
    DELETE /openApi/user/auth/userDataStream

    https://bingx-api.github.io/docs/spot/other-interface.html#delete-listen-key
    '''
    res = self.delete('/openApi/user/auth/userDataStream', params={
        'listenKey': listenKey,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res
