'''
bingX.standard.Standard
'''

from bingX import API

class Standard(API):
    def __init__(self,
        api_key:    str,
        api_secret: str,
        mode:       str = 'demo'  # Default mode is 'demo'
    ) -> object:
        if mode == "real":
            url = "https://open-api.bingx.com"
        elif mode == "demo":
            url = "https://open-api-vst.bingx.com"
        else:
            raise ValueError("Invalid mode. Mode must be 'real' or 'demo'.")
        
        super().__init__(
            api_key    = api_key,
            api_secret = api_secret,
            base_url   = url,
        )


    # ========== STANDARD CONTRACT INTERFACE ==========
    from bingX.standard.trade import (
        position,
        order_history,
        balance,
    )
