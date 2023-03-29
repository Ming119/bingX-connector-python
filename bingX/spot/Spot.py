'''
bingX.spot.Spot
'''

from bingX import API

class Spot(API):
    def __init__(self,
        api_key:    str,
        api_secret: str,
    ) -> object:
        super().__init__(
            api_key    = api_key,
            api_secret = api_secret,
            base_url   = 'https://open-api.bingx.com',
        )

    # ========== TRADE INTERFACE ==========
    from bingX.spot.trade import (
        place_order,
        cancel_order,
        order,
        open_orders,
        order_history,
        assets,
    )

    # ========== MARKET INTERFACE ==========
    from bingX.spot.market import (
        symbols,
        trades,
        depth,
    )

    # ========== USER UNIVERSAL TRANSFER INTERFACE ==========
    from bingX.spot.transfer import (
        transfer,
        transfer_history,
        deposit_history,
        withdraw_history,
    )

    # ========== OTHER INTERFACE ==========
    from bingX.spot.other import (
        generate_listen_key,
        extend_listen_key,
        delete_listen_key,
    )
