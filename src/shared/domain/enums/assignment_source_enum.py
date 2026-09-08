from enum import Enum


class AssignmentSource(Enum):
    """
    Como uma OS ganhou responsável (especificação Uberlândia §6.1) — permite
    ao Apex distinguir uma OS que ele direcionou de uma que a equipe pegou
    sozinha, e detectar quando um direcionamento seu foi rompido.
    """

    ORIGIN_SYSTEM = "ORIGIN_SYSTEM"
    CLAIM = "CLAIM"
    MANAGER = "MANAGER"
