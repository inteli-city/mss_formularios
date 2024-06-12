import datetime
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.repositories.form_repository_interface import IFormRepository
from src.shared.domain.repositories.profile_repository_interface import IProfileRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, NoItemsFound


class UpdateFormStatusUsecase:
    def __init__(self, form_repository: IFormRepository, profile_repo: IProfileRepository):
        self.form_repository = form_repository
        self.profile_repo = profile_repo

    def __call__(self, requester_id: str, form_id: str, status: FORM_STATUS):
        profile = self.profile_repo.get_profile_by_id(requester_id)

        if profile is None:
            raise ForbiddenAction("Perfil não encontrado")
        
        if not profile.enabled:
            raise ForbiddenAction("Usuário desabilitado")
        
        form = self.form_repository.get_form_by_id(user_id=requester_id, form_id=form_id)

        if form is None:
            raise NoItemsFound("Formulário não encontrado")
        
        if form.system not in profile.systems:
            raise ForbiddenAction("Usuário não tem permissão para alterar o status desse formulário")
        
        if profile.profile_id != form.user_id:
            raise ForbiddenAction("Usuário não pode alterar o status de um formulário não direcionado a ele")
        
        if status is FORM_STATUS.CANCELED or status is FORM_STATUS.CONCLUDED:
            raise ForbiddenAction("Não é possível alterar o status para cancelado ou concluído")

        if status == form.status:
            raise DuplicatedItem("O status do formulário já é o mesmo que o informado")
        
        if status is FORM_STATUS.NOT_STARTED and form.status is FORM_STATUS.IN_PROGRESS:
            start_date = None
        else:
            start_date = datetime.datetime.now().timestamp()
        
        return self.form_repository.update_form_status(user_id=requester_id, form_id=form_id, status=status, start_date=start_date)
        