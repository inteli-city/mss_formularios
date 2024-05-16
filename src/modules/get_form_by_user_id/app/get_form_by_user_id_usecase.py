from typing import List
from src.shared.domain.entities.form import Form
from src.shared.domain.repositories.form_repository_interface import IFormRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetFormByUserIdUsecase:
    def __init__(self, form_repo: IFormRepository):
        self.form_repo = form_repo

    def __call__(self, requester_user_id: str) -> List[Form]:

        forms = self.form_repo.get_form_by_user_id(user_id=requester_user_id)

        if not forms:
            raise NoItemsFound("Nenhum formulário encontrado")
        
        return forms