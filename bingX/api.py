'''
bingX.api
'''

import time
import requests
import hmac
import urllib
import base64

class API(object):
    def __init__(self, api_key: str, api_secret: str, base_url: str, api_type: str=None):
        self.api_key    = api_key
        self.api_secret = api_secret
        self.base_url   = base_url
        self.api_type   = api_type

        self.headers = {
            'X-BX-APIKEY': self.api_key,
        }

    def _handle_params(self, params, path=None, method=None):
        params = params or {}
        params['timestamp'] = round(time.time() * 1000)
        if self.api_type == 'perpetual_v1':
            params['apiKey'] = self.api_key
            params = '&'.join(f'{k}={params[k]}' for k in sorted(params) if params[k])
        else:
            params = '&'.join(f'{k}={v}' for k, v in params.items() if v)
        params += self._signature(params, path, method)
        return params

    def _signature(self, params, path=None, method=None):
        if self.api_type != 'perpetual_v1':
            sign = hmac.new(self.api_secret.encode(), params.encode(), 'sha256')
            return f'&signature={sign.hexdigest()}'
        originString = f'{method}{path}{params}'
        sign = hmac.new(self.api_secret.encode(), originString.encode(), 'sha256')   
        return f'&sign={urllib.parse.quote(base64.b64encode(sign.digest()))}'

    def _request(self, method, path, params=None, headers=None):
        url = f'{self.base_url}{path}?{self._handle_params(params, path, method)}'
        if method == 'GET':
            r = requests.get(url, headers=headers or self.headers)
        elif method == 'POST':
            r = requests.post(url, headers=headers or self.headers)
        elif method == 'PUT':
            r = requests.put(url, headers=headers or self.headers)
        elif method == 'DELETE':
            r = requests.delete(url, headers=headers or self.headers)
        else:
            raise Exception('Invalid method: %s' % method)
        return r.json()

    def get(self, path, params=None):
        return self._request('GET', path, params=params)
    
    def post(self, path, params=None):
        return self._request('POST', path, params=params)

    def put(self, path, params=None):
        return self._request('PUT', path, params=params)

    def delete(self, path, params=None):
        return self._request('DELETE', path, params=params)