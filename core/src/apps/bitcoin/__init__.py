from trezor import wire
from trezor.messages import MessageType


def boot() -> None:
    ns = [
        ["curve25519"],
        ["ed25519"],
        ["ed25519-keccak"],
        ["nist256p1"],
        ["secp256k1"],
        ["secp256k1-decred"],
        ["secp256k1-groestl"],
        ["secp256k1-smart"],
    ]
    wire.add(MessageType.GetPublicKey, __name__, "get_public_key", ns)
    wire.add(MessageType.GetAddress, __name__, "get_address", ns)
    wire.add(MessageType.SignTx, __name__, "sign_tx", ns)
    wire.add(MessageType.SignMessage, __name__, "sign_message", ns)
    wire.add(MessageType.VerifyMessage, __name__, "verify_message")
