# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeSafetyCheckLevel = Literal[0, 1, 2]
    except ImportError:
        pass


class ApplySettings(p.MessageType):
    MESSAGE_WIRE_TYPE = 25

    def __init__(
        self,
        *,
        language: str = None,
        label: str = None,
        use_passphrase: bool = None,
        homescreen: bytes = None,
        auto_lock_delay_ms: int = None,
        display_rotation: int = None,
        passphrase_always_on_device: bool = None,
        safety_checks: EnumTypeSafetyCheckLevel = None,
    ) -> None:
        self.language = language
        self.label = label
        self.use_passphrase = use_passphrase
        self.homescreen = homescreen
        self.auto_lock_delay_ms = auto_lock_delay_ms
        self.display_rotation = display_rotation
        self.passphrase_always_on_device = passphrase_always_on_device
        self.safety_checks = safety_checks

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('language', p.UnicodeType, None),
            2: ('label', p.UnicodeType, None),
            3: ('use_passphrase', p.BoolType, None),
            4: ('homescreen', p.BytesType, None),
            6: ('auto_lock_delay_ms', p.UVarintType, None),
            7: ('display_rotation', p.UVarintType, None),
            8: ('passphrase_always_on_device', p.BoolType, None),
            9: ('safety_checks', p.EnumType("SafetyCheckLevel", (0, 1, 2)), None),
        }
