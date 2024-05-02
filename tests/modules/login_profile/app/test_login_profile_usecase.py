import pytest
from src.modules.login_profile.app.login_profile_usecase import LoginProfileUsecase
from src.shared.domain.entities.profile import Profile
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.profile_repository_mock import ProfileRepositoryMock


class Test_LoginProfileUsecase:
    
    def test_login_profile_usecase(self):
        repo = ProfileRepositoryMock()
        usecase = LoginProfileUsecase(repo=repo)

        profile = usecase(
            requester_user_id=repo.profiles[0].profile_id,
            name=repo.profiles[0].name,
            email=repo.profiles[0].email,
            systems=repo.profiles[0].systems
        )

        assert profile.profile_id == repo.profiles[0].profile_id
        assert profile.name == repo.profiles[0].name
        assert profile.email == repo.profiles[0].email
        assert profile.role == repo.profiles[0].role
        assert profile.systems == repo.profiles[0].systems
        assert profile.enabled == repo.profiles[0].enabled
    
    def test_login_profile_usecase_not_enabled(self):
        repo = ProfileRepositoryMock()
        usecase = LoginProfileUsecase(repo=repo)

        with pytest.raises(ForbiddenAction):
            usecase(
                requester_user_id=repo.profiles[2].profile_id,
                name=repo.profiles[2].name,
                email=repo.profiles[2].email,
                systems=repo.profiles[2].systems
            )
    
    def test_login_profile_usecase_different_systems(self):
        repo = ProfileRepositoryMock()
        usecase = LoginProfileUsecase(repo=repo)

        profile = usecase(
            requester_user_id=repo.profiles[0].profile_id,
            name=repo.profiles[0].name,
            email=repo.profiles[0].email,
            systems=['TEST', 'JUNDIAI']
        )

        assert profile.profile_id == repo.profiles[0].profile_id
        assert profile.name == repo.profiles[0].name
        assert profile.email == repo.profiles[0].email
        assert profile.role == repo.profiles[0].role
        assert profile.systems.__contains__('TEST')
        assert profile.systems.__contains__('JUNDIAI')

    
    def test_login_profile_usecase_create_user(self):
        repo = ProfileRepositoryMock()
        usecase = LoginProfileUsecase(repo=repo)

        profile = usecase(
            requester_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120004',
            name=repo.profiles[0].name,
            email=repo.profiles[0].email,
            systems=repo.profiles[0].systems
        )

        assert profile.profile_id == 'd61dbf66-a10f-11ed-a8fc-0242ac120004'
        assert profile.name == repo.profiles[0].name
        assert profile.email == repo.profiles[0].email
        assert profile.role == ROLE.FILLER
        assert profile.systems == repo.profiles[0].systems
        assert profile.enabled == True
    
