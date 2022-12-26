'''
bingX.perpetual.other
'''

def generate_listen_key(self) -> dict:
    ''' Generate Listen Key
    POST /api/v1/user/auth/userDataStream

    https://bingx-api.github.io/docs/swap/other-interface.html#generate-listen-key
    '''
    return self.post("/api/v1/user/auth/userDataStream")

def extend_listen_key(self,
    listenKey: str,    
) -> dict:
    ''' Extend Listen Key
    PUT /api/v1/user/auth/userDataStream

    https://bingx-api.github.io/docs/swap/other-interface.html#extend-listen-key-validity-period
    '''
    return self.put("/api/v1/user/auth/userDataStream", params={
        "listenKey": listenKey,
    })

def delete_listen_key(self,
    listenKey: str,
) -> dict:
    ''' Delete Listen Key
    DELETE /api/v1/user/auth/userDataStream

    https://bingx-api.github.io/docs/swap/other-interface.html#delete-listen-key
    '''
    return self.delete("/api/v1/user/auth/userDataStream", params={
        "listenKey": listenKey,
    })