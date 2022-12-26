'''

'''

import unittest, os
from bingX.standard import Standard

class TestStandard(unittest.TestCase):
    
    def setUp(self) -> None:
        self.api_key    = os.environ['API_KEY']
        self.api_secret = os.environ['API_SECRET']
        self.standard   = Standard(api_key=self.api_key, api_secret=self.api_secret)

    def tearDown(self) -> None:
        del self.standard

    def test_position(self):
        res = self.standard.position()
        self.assertEqual(res['code'], 0)
    
    def test_order_history(self):
        res = self.standard.order_history('BTC-USDT')
        self.assertEqual(res['code'], 0)

if __name__ == '__main__':
    unittest.main()