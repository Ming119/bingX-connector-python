'''
bingX.spot.other
'''

def generate_listen_key(self):
    ''' Generate Listen Key
    POST /openApi/user/auth/userDataStream

    https://bingx-api.github.io/docs/spot/other-interface.html#generate-listen-key
    '''
    return self.post('/openApi/user/auth/userDataStream')

def extend_listen_key(self,
    listenKey: str,
) -> None:
    ''' Extend Listen Key Validity period
    PUT /openApi/user/auth/userDataStream

    https://bingx-api.github.io/docs/spot/other-interface.html#extend-listen-key-validity-period
    '''
    return self.put('/openApi/user/auth/userDataStream', params={
        'listenKey': listenKey,
    })

def delete_listen_key(self,
    listenKey: str,
) -> None:
    ''' Delete Listen Key
    DELETE /openApi/user/auth/userDataStream

    https://bingx-api.github.io/docs/spot/other-interface.html#delete-listen-key
    '''
    return self.delete('/openApi/user/auth/userDataStream', params={
        'listenKey': listenKey,
    })