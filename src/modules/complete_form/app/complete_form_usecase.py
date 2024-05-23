from typing import List, Optional
from src.shared.domain.entities.form import Form
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.repositories.form_repository_interface import IFormRepository
from src.shared.domain.repositories.profile_repository_interface import IProfileRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class CompleteFormUsecase:

    def __init__(self, form_repo: IFormRepository,  profile_repo: IProfileRepository):
        self.form_repo = form_repo
        self.profile_repo = profile_repo
    
    def __call__(self, requester_id: str, form_id: str, sections: List[Section], vinculation_form_id: Optional[str] = None) -> Form:

        profile = self.profile_repo.get_profile_by_id(requester_id)

        if profile is None:
            raise ForbiddenAction("Perfil não encontrado")
        
        if not profile.enabled:
            raise ForbiddenAction("Usuário desabilitado")
        
        form = self.form_repo.get_form_by_id(form_id)

        if form is None:
            raise NoItemsFound("Formulário não encontrado")
        
        if requester_id != form.user_id:
            raise ForbiddenAction("Usuário não pode concluir um formulário não direcionado a ele")
        
        if form.status == FORM_STATUS.CANCELED or form.status == FORM_STATUS.CONCLUDED:
            raise ForbiddenAction("Formulário já finalizado")
        for section in sections:
            print(section)
            for field in section.fields:
                if field.required and field.value is None:
                    raise ForbiddenAction("Campo obrigatório não preenchido")
                
        if vinculation_form_id is not None:
            vinculation_form = self.form_repo.get_form_by_id(vinculation_form_id)
            if vinculation_form is None:
                raise NoItemsFound("Formulário de vinculação não encontrado")
        
        return self.form_repo.complete_form(form_id=form_id, sections=sections, vinculation_form_id=vinculation_form_id)