'''
bingX.standard.Standard
'''

from bingX import API

class Standard(API):
    def __init__(self,
        api_key:    str,
        api_secret: str,
        base_url:   str = None
    ) -> object:
        super().__init__(
            api_key    = api_key,
            api_secret = api_secret,
            base_url   = base_url or "https://open-api.bingx.com",
            api_type   = "standard"
        )

    # ========== STANDARD CONTRACT INTERFACE ==========
    from bingX.standard.trade import (
        position,
        order_history,
    )