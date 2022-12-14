'''
tests/test_spot.py
'''

import unittest, os
from bingX.spot import Spot

class TestStandard(unittest.TestCase):
    
    def setUp(self) -> None:
        self.api_key    = os.environ['API_KEY']
        self.api_secret = os.environ['API_SECRET']
        self.spot       = Spot(api_key=self.api_key, api_secret=self.api_secret)

        self.listenKey = self.spot.generate_listen_key()['listenKey']

    def tearDown(self) -> None:
        del self.spot

    # ========== MARKET ==========
    def test_symbols(self):
        res = self.spot.symbols()
        self.assertEqual(res['code'], 0)
    
    def test_trades(self):
        res = self.spot.trades(symbol='BTC-USDT')
        self.assertEqual(res['code'], 0)
    
    def test_depth(self):
        res = self.spot.depth(symbol='BTC-USDT')
        self.assertEqual(res['code'], 0)

    # ========== TRADE ==========
    def test_balance(self):
        res = self.spot.balance()
        self.assertEqual(res['code'], 0)

    def test_open_order(self):
        res = self.spot.open_orders(symbol='BTC-USDT')
        self.assertEqual(res['code'], 0)

    def test_order_history(self):
        res = self.spot.order_history(symbol='BTC-USDT')
        self.assertEqual(res['code'], 0)

    # ========== OTHER ==========
    def test_generate_listen_key(self):
        self.assertIsNotNone(self.listenKey)
    
    def test_extend_listen_key(self):
        res = self.spot.extend_listen_key(self.listenKey)
        print(res)
        self.assertEqual(res['code'], 0)
    
    def test_delete_listen_key(self):
        res = self.spot.delete_listen_key()
        self.assertEqual(res['code'], 0)

if __name__ == '__main__':
    unittest.main()