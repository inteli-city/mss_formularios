from src.modules.cancel_form.app.cancel_form_controller import CancelFormController
from src.modules.cancel_form.app.cancel_form_usecase import CancelFormUsecase
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.form_repository_mock import FormRepositoryMock
from src.shared.infra.repositories.image_repository_mock import ImageRepositoryMock
from src.shared.infra.repositories.profile_repository_mock import ProfileRepositoryMock


class Test_CancelFormController:

    def test_cancel_form_controller(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)

        controller = CancelFormController(usecase)

        form_repo.forms[0].status = FORM_STATUS.IN_PROGRESS

        data = HttpRequest(body={"requester_user": {
                "sub": profile_repo.profiles[0].profile_id,
                "name": 'Gabriel Godoy',
                "email": 'gabriel@gmail.com',
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "form_id": form_repo.forms[0].form_id,
            "selected_option": "option",
            "justification_text": "justification_test",
            "justification_image": "image_test"
        })

        response = controller(data)

        assert response.status_code == 200
        assert response.body['message'] == 'Formulário cancelado com sucesso!'
    
    def test_cancel_form_controller_missing_request_user(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)

        controller = CancelFormController(usecase)

        data = HttpRequest(body={"form_id": form_repo.forms[0].form_id,
            "selected_option": "option",
            "justification_text": "justification_test",
            "justification_image": "image_test"
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: requester_user'
    
    def test_cancel_form_controller_missing_form_id(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)

        controller = CancelFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": profile_repo.profiles[0].profile_id,
                "name": 'Gabriel Godoy',
                "email": 'gabriel@gmail.com',
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "selected_option": "option",
            "justification_text": "justification_test",
            "justification_image": "image_test"
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: form_id'
    
    def test_cancel_form_controller_missing_selected_option(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)

        controller = CancelFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": profile_repo.profiles[0].profile_id,
                "name": 'Gabriel Godoy',
                "email": 'gabriel@gmail.com',
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "form_id": form_repo.forms[0].form_id,
            "justification_text": "justification_test",
            "justification_image": "image_test"
        })
    
        response = controller(data)

        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: selected_option'
    
    def test_cancel_form_controller_wrong_type_selected_option(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)

        controller = CancelFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": profile_repo.profiles[0].profile_id,
                "name": 'Gabriel Godoy',
                "email": 'gabriel@gmail.com',
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "form_id": form_repo.forms[0].form_id,
            "selected_option": 123,
            "justification_text": "justification_test",
            "justification_image": "image_test"
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body == 'Campo selected_option deveria ser do tipo str, mas foi recebido um campo do tipo <class \'int\'>'
    
    def test_cancel_form_controller_wrong_type_justification_text(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)

        controller = CancelFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": profile_repo.profiles[0].profile_id,
                "name": 'Gabriel Godoy',
                "email": 'gabriel@gmail.com',
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "form_id": form_repo.forms[0].form_id,
            "selected_option": "selected",
            "justification_text": 123,
            "justification_image": "image_test"
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body == 'Campo justification_text deveria ser do tipo str, mas foi recebido um campo do tipo <class \'int\'>'
    
    def test_cancel_form_controller_wrong_type_justification_image(self):
        form_repo = FormRepositoryMock()
        profile_repo = ProfileRepositoryMock()
        image_repo = ImageRepositoryMock()
        usecase = CancelFormUsecase(form_repo, profile_repo, image_repo)

        controller = CancelFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": profile_repo.profiles[0].profile_id,
                "name": 'Gabriel Godoy',
                "email": 'gabriel@gmail.com',
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "form_id": form_repo.forms[0].form_id,
            "selected_option": "selected",
            "justification_text": "justification_test",
            "justification_image": 123
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body == 'Campo justification_image deveria ser do tipo str, mas foi recebido um campo do tipo <class \'int\'>'
