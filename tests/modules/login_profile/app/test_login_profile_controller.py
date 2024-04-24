from src.modules.login_profile.app.login_profile_controller import LoginProfileController
from src.modules.login_profile.app.login_profile_usecase import LoginProfileUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.profile_repository_mock import ProfileRepositoryMock


class Test_LoginProfileController:

    def test_login_profile_controller(self):
        repo = ProfileRepositoryMock()
        usecase = LoginProfileUsecase(repo)

        controller = LoginProfileController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": repo.profiles[0].name,
                "email": repo.profiles[0].email,
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },   
        })

        response = controller(data)
        print(response)
        assert response.status_code == 200
        assert response.body["profile"]["profile_id"] == 'd61dbf66-a10f-11ed-a8fc-0242ac120001'
        assert response.body["profile"]["name"] == repo.profiles[0].name
        assert response.body["profile"]["email"] == repo.profiles[0].email
        assert response.body["profile"]["role"] == 'FILLER'
        assert response.body["profile"]["systems"] == ['GAIA', 'JUNDIAI', 'FORMULARIOS']
        assert response.body["profile"]["enabled"] == True

    def test_login_profile_controller_no_requester_user(self):
        repo = ProfileRepositoryMock()
        usecase = LoginProfileUsecase(repo)

        controller = LoginProfileController(usecase)

        data = HttpRequest(body={})

        response = controller(data)
        print(response)
        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: requester_user"
    
    def test_login_profile_controller_user_not_in_formularios(self):
        repo = ProfileRepositoryMock()
        usecase = LoginProfileUsecase(repo)

        controller = LoginProfileController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": repo.profiles[0].name,
                "email": repo.profiles[0].email,
                "cognito:groups": "JUNDIAI"
            },   
        })

        response = controller(data)
        print(response)
        assert response.status_code == 403
        assert response.body == "Ação não permitida: Usuário não esta apto para o sistema"