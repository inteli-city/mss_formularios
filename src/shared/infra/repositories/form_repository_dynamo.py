from src.shared.domain.repositories.form_repository_interface import IFormRepository


class FormRepositoryDynamo(IFormRepository):

    def __init__(self):
        pass

    def get_form_by_user_id(self, user_id: str) -> dict:
        pass