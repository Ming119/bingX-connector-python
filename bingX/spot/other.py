'''
bingX.spot.other
'''

def generate_listen_key(self):
    ''' Generate Listen Key
    listen key Valid for 1 hour

    POST /openApi/user/auth/userDataStream

    https://bingx-api.github.io/docs/spot/other-interface.html#generate-listen-key
    '''
    return self.post('/openApi/user/auth/userDataStream')

def extend_listen_key(self):
    ''' Extend Listen Key Validity Period
    The validity period is extended to 60 minutes after this call, and it is
    recommended to send a ping every 30 minutes.

    PUT /openApi/user/auth/userDataStream

    https://bingx-api.github.io/docs/spot/other-interface.html#extend-listen-key-validity-period
    '''
    return self.put('/openApi/user/auth/userDataStream')

def delete_listen_key(self):
    ''' Delete Listen Key
    delete User data flow.

    DELETE /openApi/user/auth/userDataStream

    https://bingx-api.github.io/docs/spot/other-interface.html#delete-listen-key
    '''
    return self.delete('/openApi/user/auth/userDataStream')