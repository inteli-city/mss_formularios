from src.shared.domain.entities.form_event import FormEvent
from src.shared.domain.enums.form_event_type_enum import FormEventType


class FormEventDynamoDTO:
    """
    PK = form#{form_id} | SK = event#{created_at:013d}#{id}
    Mesma partição do Form — write-only por enquanto (§6.4).
    """

    def __init__(
        self,
        id: str,
        form_id: str,
        event_type: FormEventType,
        actor_user_id: str,
        created_at: int,
        target_user_id=None,
        payload=None,
    ):
        self.id = id
        self.form_id = form_id
        self.event_type = event_type
        self.actor_user_id = actor_user_id
        self.created_at = created_at
        self.target_user_id = target_user_id
        self.payload = payload if payload is not None else {}

    @staticmethod
    def from_entity(event: FormEvent) -> "FormEventDynamoDTO":
        return FormEventDynamoDTO(
            id=event.id,
            form_id=event.form_id,
            event_type=event.event_type,
            actor_user_id=event.actor_user_id,
            created_at=event.created_at,
            target_user_id=event.target_user_id,
            payload=event.payload,
        )

    def to_dynamo(self) -> dict:
        return {
            "id": self.id,
            "form_id": self.form_id,
            "event_type": self.event_type.value,
            "actor_user_id": self.actor_user_id,
            "target_user_id": self.target_user_id,
            "payload": self.payload,
            "created_at": self.created_at,
        }

    @staticmethod
    def build_pk(form_id: str) -> str:
        return f"form#{form_id}"

    @staticmethod
    def build_sk(created_at: int, event_id: str) -> str:
        return f"event#{int(created_at):013d}#{event_id}"
