from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UserRepositoryMock:
    def test_get_groups_for_user(self):
        repo = UserRepositoryMock()
        groups = repo.get_groups_for_user('gabriel@gmail.com')

        assert len(groups) == 3
        assert 'GAIA' in groups
        assert 'FORMULARIOS' in groups