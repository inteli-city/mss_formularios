from enum import Enum


class FormEventType(Enum):
    """Histórico imutável de posse (RN-UBE-008, especificação Uberlândia §6.4)."""

    CLAIMED = "CLAIMED"
    RELEASED = "RELEASED"
    ASSIGNED = "ASSIGNED"
