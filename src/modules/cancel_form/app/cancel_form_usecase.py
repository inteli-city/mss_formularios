from typing import Optional
from src.shared.domain.entities.form import Form
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.repositories.form_repository_interface import IFormRepository
from src.shared.domain.repositories.profile_repository_interface import IProfileRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class CancelFormUsecase:
    def __init__(self, form_repo: IFormRepository, profile_repo: IProfileRepository):
        self.form_repo = form_repo
        self.profile_repo = profile_repo

    def __call__(self, requester_id: str, form_id: str, selected_option: str, justification_text: Optional[str] = None, justification_image: Optional[str] = None) -> Form:

        profile = self.profile_repo.get_profile_by_id(requester_id)

        if profile is None:
            raise ForbiddenAction("Perfil não encontrado")
        
        if not profile.enabled:
            raise ForbiddenAction("Usuário desabilitado")
        
        form = self.form_repo.get_form_by_id(form_id)

        if form is None:
            raise NoItemsFound("Formulário não encontrado")
        
        if requester_id != form.user_id:
            raise ForbiddenAction("Usuário não pode cancelar um formulário não direcionado a ele")
        
        if form.status == FORM_STATUS.CANCELED or form.status == FORM_STATUS.CONCLUDED:
            raise ForbiddenAction("Formulário já finalizado")
        
        return self.form_repo.cancel_form(form_id=form_id, selected_option=selected_option, justification_text=justification_text, justification_image=justification_image)
