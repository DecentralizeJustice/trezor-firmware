# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EosPermissionLevel(p.MessageType):

    def __init__(
        self,
        *,
        actor: int = None,
        permission: int = None,
    ) -> None:
        self.actor = actor
        self.permission = permission

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('actor', p.UVarintType, None),
            2: ('permission', p.UVarintType, None),
        }
