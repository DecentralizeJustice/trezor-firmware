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
    wire.add(MessageType.GetEntropy, __name__, "get_entropy")
    wire.add(MessageType.SignIdentity, __name__, "sign_identity", ns)
    wire.add(MessageType.GetECDHSessionKey, __name__, "get_ecdh_session_key", ns)
    wire.add(MessageType.CipherKeyValue, __name__, "cipher_key_value", ns)
