from src.shared.domain.entities.form import Form
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.repositories.form_repository_interface import IFormRepository


class FormRepositoryDynamo(IFormRepository):

    def __init__(self):
        pass

    def get_form_by_user_id(self, user_id: str) -> dict:
        pass

    def create_form(self, form: Form) -> Form:
        pass

    def update_form_status(self, form_id: str, status: FORM_STATUS) -> Form:
        pass