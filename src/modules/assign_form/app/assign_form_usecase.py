import uuid
from typing import List, Optional

from src.shared.domain.entities.form import Form
from src.shared.domain.entities.form_event import FormEvent
from src.shared.domain.enums.assignment_source_enum import AssignmentSource
from src.shared.domain.enums.form_event_type_enum import FormEventType
from src.shared.domain.enums.profile_role_enum import ProfileRole
from src.shared.domain.repositories.form_event_repository_interface import IFormEventRepository
from src.shared.domain.repositories.form_repository_interface import IFormRepository
from src.shared.domain.repositories.profile_repository_interface import IProfileRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.functions.datetime_utils import now_timestamp_ms

_MANAGER_ROLES = {ProfileRole.ADMIN, ProfileRole.MANAGER, ProfileRole.SUPERVISOR}


class AssignFormUsecase:
    """Gestor/Fiscal atribui diretamente uma OS do pool a um usuário (RN-UBE-005)."""

    def __init__(
        self,
        form_repo: IFormRepository,
        profile_repo: IProfileRepository,
        form_event_repo: IFormEventRepository,
    ):
        self.form_repo = form_repo
        self.profile_repo = profile_repo
        self.form_event_repo = form_event_repo

    def __call__(
        self, requester_user_id: str, requester_systems: Optional[List[str]], form_id: str, target_user_id: str,
    ) -> Form:
        self._ensure_requester_can_assign(requester_user_id)

        form = self.form_repo.get_form_by_id(user_id=requester_user_id, form_id=form_id)
        if form is None:
            raise NoItemsFound("Formulário não encontrado")
        if requester_systems is not None and form.system not in requester_systems:
            raise ForbiddenAction("Usuário não tem permissão para acessar este sistema")

        now_ms = now_timestamp_ms()
        assigned = self.form_repo.claim_form(
            form_id=form_id,
            user_id=target_user_id,
            claimed_at=now_ms,
            updated_at=now_ms,
            source=AssignmentSource.MANAGER,
        )
        if assigned is None:
            raise NoItemsFound("Formulário não encontrado")

        self.form_event_repo.create_event(FormEvent(
            id=str(uuid.uuid4()),
            form_id=form_id,
            event_type=FormEventType.ASSIGNED,
            actor_user_id=requester_user_id,
            target_user_id=target_user_id,
            created_at=now_ms,
        ))
        return assigned

    def _ensure_requester_can_assign(self, requester_user_id: str) -> None:
        profile = self.profile_repo.get_by_user_id(requester_user_id)
        if profile is None or not profile.active or profile.role not in _MANAGER_ROLES:
            raise ForbiddenAction("Apenas Gestor, Fiscal ou Admin podem atribuir formulários do pool")
