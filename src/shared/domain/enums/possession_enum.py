from enum import Enum


class Possession(Enum):
    """
    Segundo eixo de estado do Form, companheiro de `status` (especificação
    Uberlândia §6.1.1) — decide se a OS está no pool ou já tem dono.

    OPEN  ⟺ user_id ausente do item ⟺ está no pool, visível a quem o
             escopo cobrir.
    OWNED ⟺ user_id presente, direcionada (criação) ou reivindicada (claim/assign).
    """

    OPEN = "OPEN"
    OWNED = "OWNED"
