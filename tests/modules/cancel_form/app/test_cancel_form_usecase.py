import pytest
from src.modules.cancel_form.app.cancel_form_usecase import CancelFormUsecase
from src.shared.domain.entities.justification import Justification, JustificationOption
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.form_repository_mock import FormRepositoryMock
from src.shared.infra.repositories.image_repository_mock import ImageRepositoryMock
from src.shared.infra.repositories.profile_repository_mock import ProfileRepositoryMock

justification_option = JustificationOption(
    option='option',
    required_image=True,
    required_text=True
)

justification = Justification(
    options=[justification_option],
    selected_option='option',
    justification_text='text',
    justification_image='image'
)

class Test_CancelFormUsecase:

    def test_cancel_form_usecase(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)

        form_repo.forms[0].status = FORM_STATUS.IN_PROGRESS

        form = usecase(
            requester_id=profile_repo.profiles[0].profile_id,
            form_id=form_repo.forms[0].form_id,
            justification_image=justification.justification_image,
            selected_option=justification.selected_option,
            justification_text=justification.justification_text
        )

        assert form.form_id == form_repo.forms[0].form_id
        assert form.status == FORM_STATUS.CANCELED
        assert form.justification.selected_option == 'option'
        assert form.justification.justification_text == 'text'
        assert form.justification.justification_image.startswith('https://test')

    
    def test_cancel_form_usecase_profile_not_found(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)
        
        with pytest.raises(ForbiddenAction):
            usecase(
                requester_id='invalid_id',
                form_id=form_repo.forms[0].form_id,
                justification_image=justification.justification_image,
                selected_option=justification.selected_option,
                justification_text=justification.justification_text
            )
    
    def test_cancel_form_usecase_profile_not_enabled(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)
        
        profile_repo.profiles[0].enabled = False
        
        with pytest.raises(ForbiddenAction):
            usecase(
                requester_id=profile_repo.profiles[2].profile_id,
                form_id=form_repo.forms[0].form_id,
                justification_image=justification.justification_image,
                selected_option=justification.selected_option,
                justification_text=justification.justification_text
            )
    
    def test_cancel_form_usecase_form_not_found(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)
        
        with pytest.raises(NoItemsFound):
            usecase(
                requester_id=profile_repo.profiles[0].profile_id,
                form_id='invalid_id',
                justification_image=justification.justification_image,
                selected_option=justification.selected_option,
                justification_text=justification.justification_text
            )
    
    def test_cancel_form_usecase_user_cannot_cancel_form(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)
        
        with pytest.raises(ForbiddenAction):
            usecase(
                requester_id=profile_repo.profiles[1].profile_id,
                form_id=form_repo.forms[0].form_id,
                justification_image=justification.justification_image,
                selected_option=justification.selected_option,
                justification_text=justification.justification_text
            )

    def test_cancel_form_usecase_form_already_finished(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)
        
        form_repo.forms[0].status = FORM_STATUS.CANCELED
        
        with pytest.raises(ForbiddenAction):
            usecase(
                requester_id=profile_repo.profiles[0].profile_id,
                form_id=form_repo.forms[0].form_id,
                justification_image=justification.justification_image,
                selected_option=justification.selected_option,
                justification_text=justification.justification_text
            )
    
    def test_cancel_form_usecase_form_invalid_justification_option(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)
        
        justification.selected_option = 'invalid_option'
        
        with pytest.raises(EntityError):
            usecase(
                requester_id=profile_repo.profiles[0].profile_id,
                form_id=form_repo.forms[0].form_id,
                justification_image=justification.justification_image,
                selected_option=justification.selected_option,
                justification_text=justification.justification_text
            )
    
    def test_cancel_form_usecase_form_missing_text_justification(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)
        
        justification.justification_text = ''
        
        with pytest.raises(EntityError):
            usecase(
                requester_id=profile_repo.profiles[0].profile_id,
                form_id=form_repo.forms[0].form_id,
                justification_image=justification.justification_image,
                selected_option=justification.selected_option,
                justification_text=justification.justification_text
            )
    
    def test_cancel_form_usecase_form_missing_image_justification(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)
        
        justification.justification_image = ''
        
        with pytest.raises(EntityError):
            usecase(
                requester_id=profile_repo.profiles[0].profile_id,
                form_id=form_repo.forms[0].form_id,
                justification_image=justification.justification_image,
                selected_option=justification.selected_option,
                justification_text=justification.justification_text
            )