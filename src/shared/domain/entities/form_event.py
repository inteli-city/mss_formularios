import abc
from typing import Any, Dict, Optional

from src.shared.domain.enums.form_event_type_enum import FormEventType
from src.shared.helpers.errors.domain_errors import EntityError


class FormEvent(abc.ABC):
    """
    Histórico imutável de transição de posse de um Form (RN-UBE-008,
    especificação Uberlândia §6.4). Mesma partição do formulário
    (`PK = form#{form_id}`), barato e auditável — write-only nesta fase,
    sem endpoint de leitura ainda (não há consumidor).
    """

    id: str
    form_id: str
    event_type: FormEventType
    actor_user_id: str
    target_user_id: Optional[str]
    payload: Dict[str, Any]
    created_at: int

    def __init__(
        self,
        id: str,
        form_id: str,
        event_type: FormEventType,
        actor_user_id: str,
        created_at: int,
        target_user_id: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
    ):
        if not isinstance(id, str) or not id:
            raise EntityError("ID do evento inválido ou ausente")
        self.id = id

        if not isinstance(form_id, str) or not form_id:
            raise EntityError("form_id do evento inválido ou ausente")
        self.form_id = form_id

        if not isinstance(event_type, FormEventType):
            raise EntityError("Tipo de evento inválido")
        self.event_type = event_type

        if not isinstance(actor_user_id, str) or not actor_user_id:
            raise EntityError("actor_user_id do evento inválido ou ausente")
        self.actor_user_id = actor_user_id

        if target_user_id is not None and not isinstance(target_user_id, str):
            raise EntityError("target_user_id deve ser uma string ou null")
        self.target_user_id = target_user_id

        if payload is not None and not isinstance(payload, dict):
            raise EntityError("payload do evento deve ser um dicionário")
        self.payload = payload if payload is not None else {}

        if not isinstance(created_at, int) or isinstance(created_at, bool):
            raise EntityError("Timestamp de criação do evento deve ser um inteiro")
        self.created_at = created_at
