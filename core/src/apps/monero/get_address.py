from trezor.messages.MoneroAddress import MoneroAddress

from apps.common import paths
from apps.common.layout import address_n_to_str, show_qr
from apps.common.seed import with_slip44_keychain
from apps.monero import CURVE, SLIP44, misc
from apps.monero.layout import confirms
from apps.monero.xmr import addresses, crypto, monero
from apps.monero.xmr.networks import net_version


@with_slip44_keychain(SLIP44, CURVE, allow_testnet=True)
async def get_address(ctx, msg, keychain):
    await paths.validate_path(
        ctx, misc.validate_full_path, keychain, msg.address_n, CURVE
    )

    creds = misc.get_creds(keychain, msg.address_n, msg.network_type)
    addr = creds.address

    if msg.payment_id:
        if len(msg.payment_id) != 8:
            raise ValueError("Invalid payment ID length")
        addr = addresses.encode_addr(
            net_version(msg.network_type, False, True),
            crypto.encodepoint(creds.spend_key_public),
            crypto.encodepoint(creds.view_key_public),
            msg.payment_id,
        )

    if msg.account or msg.minor:
        if msg.payment_id:
            raise ValueError("Subaddress cannot be integrated")

        pub_spend, pub_view = monero.generate_sub_address_keys(
            creds.view_key_private, creds.spend_key_public, msg.account, msg.minor
        )

        addr = addresses.encode_addr(
            net_version(msg.network_type, True, False),
            crypto.encodepoint(pub_spend),
            crypto.encodepoint(pub_view),
        )

    if msg.show_display:
        desc = address_n_to_str(msg.address_n)
        while True:
            if await confirms.show_address(ctx, addr.decode(), desc=desc):
                break
            if await show_qr(ctx, "monero:" + addr.decode(), desc=desc):
                break

    return MoneroAddress(address=addr)
