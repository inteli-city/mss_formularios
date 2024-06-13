import pytest
from src.modules.get_form_by_user_id.app.get_form_by_user_id_usecase import GetFormByUserIdUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.form_repository_mock import FormRepositoryMock


class Test_GetFormByUserIdUseCase:

    def test_get_form_by_user_id(self):
        repo = FormRepositoryMock()
        usecase = GetFormByUserIdUsecase(repo)
        forms = usecase(requester_user_id=repo.forms[0].user_id)

        assert len(forms) == 2
    
    def test_get_form_by_user_id_no_items_found(self):
        repo = FormRepositoryMock()
        usecase = GetFormByUserIdUsecase(repo)
        repo.forms = []

        forms = usecase(requester_user_id='1')

        assert len(forms) == 0
        