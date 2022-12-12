'''

'''

import unittest, os
from bingX.spot import Spot

class TestStandard(unittest.TestCase):
    
    def setUp(self) -> None:
        self.api_key    = os.environ['API_KEY']
        self.api_secret = os.environ['API_SECRET']
        self.spot   = Spot(api_key=self.api_key, api_secret=self.api_secret)

    def tearDown(self) -> None:
        del self.spot

    def test_balance(self):
        res = self.spot.balance()
        self.assertEqual(res['code'], 0)

    def test_open_order(self):
        res = self.spot.open_orders(symbol='BTC-USDT')
        self.assertEqual(res['code'], 0)

    def test_order_history(self):
        res = self.spot.order_history(symbol='BTC-USDT')
        self.assertEqual(res['code'], 0)
        
if __name__ == '__main__':
    unittest.main()