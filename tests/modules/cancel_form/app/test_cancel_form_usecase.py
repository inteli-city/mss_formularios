import pytest
from src.modules.cancel_form.app.cancel_form_usecase import CancelFormUsecase
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.form_repository_mock import FormRepositoryMock
from src.shared.infra.repositories.profile_repository_mock import ProfileRepositoryMock


class Test_CancelFormUsecase:

    def test_cancel_form_usecase(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo)

        form_repo.forms[0].status = FORM_STATUS.IN_PROGRESS

        form = usecase(
            requester_id=profile_repo.profiles[0].profile_id,
            form_id=form_repo.forms[0].form_id,
            selected_option='option_update',
            justification_text='text_update',
            justification_image='image_update'
        )

        assert form.form_id == form_repo.forms[0].form_id
        assert form.status == FORM_STATUS.CANCELED
        assert form.justification.selected_option == 'option_update'
        assert form.justification.justification_text == 'text_update'
        assert form.justification.justification_image == 'image_update'
    
    def test_cancel_form_usecase_profile_not_found(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo)
        
        with pytest.raises(ForbiddenAction):
            usecase(
                requester_id='invalid_id',
                form_id=form_repo.forms[0].form_id,
                selected_option='option_update',
                justification_text='text_update',
                justification_image='image_update'
            )
    
    def test_cancel_form_usecase_profile_not_enabled(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo)
        
        profile_repo.profiles[0].enabled = False
        
        with pytest.raises(ForbiddenAction):
            usecase(
                requester_id=profile_repo.profiles[2].profile_id,
                form_id=form_repo.forms[0].form_id,
                selected_option='option_update',
                justification_text='text_update',
                justification_image='image_update'
            )
    
    def test_cancel_form_usecase_form_not_found(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo)
        
        with pytest.raises(NoItemsFound):
            usecase(
                requester_id=profile_repo.profiles[0].profile_id,
                form_id='invalid_id',
                selected_option='option_update',
                justification_text='text_update',
                justification_image='image_update'
            )
    
    def test_cancel_form_usecase_user_cannot_cancel_form(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo)
        
        with pytest.raises(ForbiddenAction):
            usecase(
                requester_id=profile_repo.profiles[1].profile_id,
                form_id=form_repo.forms[0].form_id,
                selected_option='option_update',
                justification_text='text_update',
                justification_image='image_update'
            )

    def test_cancel_form_usecase_form_already_finished(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo)
        
        form_repo.forms[0].status = FORM_STATUS.CANCELED
        
        with pytest.raises(ForbiddenAction):
            usecase(
                requester_id=profile_repo.profiles[0].profile_id,
                form_id=form_repo.forms[0].form_id,
                selected_option='option_update',
                justification_text='text_update',
                justification_image='image_update'
            )