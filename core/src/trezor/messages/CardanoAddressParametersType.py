# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .CardanoBlockchainPointerType import CardanoBlockchainPointerType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeCardanoAddressType = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 14, 15]
    except ImportError:
        pass


class CardanoAddressParametersType(p.MessageType):

    def __init__(
        self,
        *,
        address_n: List[int] = None,
        address_n_staking: List[int] = None,
        address_type: EnumTypeCardanoAddressType = None,
        staking_key_hash: bytes = None,
        certificate_pointer: CardanoBlockchainPointerType = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.address_n_staking = address_n_staking if address_n_staking is not None else []
        self.address_type = address_type
        self.staking_key_hash = staking_key_hash
        self.certificate_pointer = certificate_pointer

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_type', p.EnumType("CardanoAddressType", (0, 1, 2, 3, 4, 5, 6, 7, 8, 14, 15)), None),
            2: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            3: ('address_n_staking', p.UVarintType, p.FLAG_REPEATED),
            4: ('staking_key_hash', p.BytesType, None),
            5: ('certificate_pointer', CardanoBlockchainPointerType, None),
        }
