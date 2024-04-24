from src.shared.infra.repositories.form_repository_mock import FormRepositoryMock


class Test_FormRepositoryMock:

    def test_get_form_by_user_id(self):
        repo = FormRepositoryMock()
        form = repo.get_form_by_user_id('1')

        assert len(form) == 1