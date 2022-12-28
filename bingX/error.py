
class ServerError(BaseException):
    def __init__(self, status_code, error_msg):
        self.status_code = status_code
        self.error_msg   = error_msg


class ClientError(BaseException):
    def __init__(self, error_code: int, error_msg: str):
        self.error_code  = error_code
        self.error_msg   = error_msg

        self.error_msg_map = {
            100001: 'Signature authentication failed',
            100202: 'Insufficient balance',
            100400: 'Invalid parameter',
            100440: 'Order price deviates greatly from the market price',
            100500: 'Internal server error',
            100503: 'Server busy',
        }
    
    def __str__(self):
        return f'{self.error_code} - {self.error_msg or self.error_msg_map[self.error_code]}'

