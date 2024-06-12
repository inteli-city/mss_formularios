import pytest
from src.modules.update_form_status.app.update_form_status_usecase import UpdateFormStatusUsecase
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.repositories.form_repository_interface import IFormRepository
from src.shared.domain.repositories.profile_repository_interface import IProfileRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.form_repository_mock import FormRepositoryMock
from src.shared.infra.repositories.profile_repository_mock import ProfileRepositoryMock


class Test_UpdateFormStatusUseCase:

    def test_update_form_status_usecase(self):
        repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = UpdateFormStatusUsecase(repo, profile_repo)

        form = repo.forms[2]
        profile = profile_repo.profiles[0]

        result = usecase(profile.profile_id, form.form_id, FORM_STATUS.IN_PROGRESS)

        assert result.status == FORM_STATUS.IN_PROGRESS
        assert result.start_date is not None
    
    def test_update_form_status_usecase_go_back(self):
        repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = UpdateFormStatusUsecase(repo, profile_repo)

        form = repo.forms[0]
        profile = profile_repo.profiles[0]

        result = usecase(profile.profile_id, form.form_id, FORM_STATUS.NOT_STARTED)

        assert result.status == FORM_STATUS.NOT_STARTED
        assert result.start_date is None
    
    def test_update_form_status_usecase_same_status(self):
        repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = UpdateFormStatusUsecase(repo, profile_repo)

        form = repo.forms[0]
        profile = profile_repo.profiles[0]

        with pytest.raises(DuplicatedItem):
            usecase(profile.profile_id, form.form_id, FORM_STATUS.IN_PROGRESS)
    
    def test_update_form_status_usecase_profile_not_found(self):
        repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = UpdateFormStatusUsecase(repo, profile_repo)

        form = repo.forms[0]

        with pytest.raises(ForbiddenAction):
            usecase('123', form.form_id, FORM_STATUS.IN_PROGRESS)
    
    def test_update_form_status_usecase_user_disabled(self):
        repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = UpdateFormStatusUsecase(repo, profile_repo)

        form = repo.forms[1]
        profile = profile_repo.profiles[2]

        with pytest.raises(ForbiddenAction):
            usecase(profile.profile_id, form.form_id, FORM_STATUS.IN_PROGRESS)
    
    def test_update_form_status_usecase_form_not_found(self):
        repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = UpdateFormStatusUsecase(repo, profile_repo)

        profile = profile_repo.profiles[0]

        with pytest.raises(NoItemsFound):
            usecase(profile.profile_id, '123', FORM_STATUS.IN_PROGRESS)
        
    
    def test_update_form_status_usecase_user_not_in_systems(self):
        repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = UpdateFormStatusUsecase(repo, profile_repo)

        with pytest.raises(ForbiddenAction):
            usecase('d61dbf66-a10f-11ed-a8fc-0242ac120003', 'd61dbf66-a10f-11ed-a8fc-0242ac120010', FORM_STATUS.IN_PROGRESS)
    
    def test_update_form_status_usecase_user_not_owner(self):
        repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = UpdateFormStatusUsecase(repo, profile_repo)

        form = repo.forms[0]
        profile = profile_repo.profiles[1]

        with pytest.raises(ForbiddenAction):
            usecase(profile.profile_id, form.form_id, FORM_STATUS.IN_PROGRESS)
    


        