'''
bingX.standard.Standard
'''

from bingX import API

class Standard(API):
    def __init__(self,
        api_key:    str,
        api_secret: str,
    ) -> object:
        super().__init__(
            api_key    = api_key,
            api_secret = api_secret,
            base_url   = "https://open-api.bingx.com",
        )

    # ========== STANDARD CONTRACT INTERFACE ==========
    from bingX.standard.trade import (
        position,
        order_history,
        balance,
    )
