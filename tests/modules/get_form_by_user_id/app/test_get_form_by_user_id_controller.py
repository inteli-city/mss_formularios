from src.modules.get_form_by_user_id.app.get_form_by_user_id_controller import GetFormByUserIdController
from src.modules.get_form_by_user_id.app.get_form_by_user_id_usecase import GetFormByUserIdUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.form_repository_mock import FormRepositoryMock
from datetime import datetime, timedelta

def timestamp_yesterday():
        current_date = datetime.now()
        yesterday_date = current_date - timedelta(days=1)

        timestamp_yesterday_seconds = int(yesterday_date.timestamp())
        timestamp_yesterday_milliseconds = timestamp_yesterday_seconds * 1000
        print(timestamp_yesterday_milliseconds)
        return timestamp_yesterday_milliseconds
class Test_GetFormByUserIdController:


    def test_get_form_by_user_id_controller(self):
        repo = FormRepositoryMock()
        usecase = GetFormByUserIdUsecase(repo)

        controller = GetFormByUserIdController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": '1',
                "name": 'Gabriel Godoy',
                "email": 'test@gmail.com',
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },   
        })

        response = controller(data)

        print(response.body)

        assert response.status_code == 200
        assert response.body == {
            'form_list': [
                {
                    'extern_form_id': '1',
                    'internal_form_id': '1',
                    'creator_user_id': '1',
                    'user_id': '1',
                    'coordinators_id': ['1'],
                    'vinculation_form_id': None,
                    'template': 'TEMPLATE',
                    'area': '1',
                    'system': '1',
                    'street': '1',
                    'city': '1',
                    'number': 1,
                    'latitude': 1.0,
                    'longitude': 1.0,
                    'region': 'REGION',
                    'description': None,
                    'priority': 'EMERGENCY',
                    'status': 'CONCLUDED',
                    'expiration_date': 946407600000,
                    'creation_date': 946407600000,
                    'start_date': 946407600000,
                    'conclusion_date': timestamp_yesterday(),
                    'justificative': None,
                    'comments': None,
                    'sections': [
                        {
                            'section_id': '99999',
                            'fields': [
                                {
                                    'field_type': 'TEXT_FIELD',
                                    'placeholder': 'placeholder',
                                    'required': True,
                                    'key': 'key',
                                    'regex': 'regex',
                                    'formatting': 'formatting',
                                    'max_length': 10,
                                    'value': 'value'
                                },
                                {
                                    'field_type': 'TEXT_FIELD',
                                    'placeholder': 'placeholder',
                                    'required': True,
                                    'key': 'key',
                                    'regex': 'regex',
                                    'formatting': 'formatting',
                                    'max_length': 10,
                                    'value': 'value'
                                }
                            ]
                        },
                        {
                            'section_id': '99999',
                            'fields': [
                                {
                                    'field_type': 'TEXT_FIELD',
                                    'placeholder': 'placeholder',
                                    'required': True,
                                    'key': 'key',
                                    'regex': 'regex',
                                    'formatting': 'formatting',
                                    'max_length': 10,
                                    'value': 'value'
                                },
                                {
                                    'field_type': 'TEXT_FIELD',
                                    'placeholder': 'placeholder',
                                    'required': True,
                                    'key': 'key',
                                    'regex': 'regex',
                                    'formatting': 'formatting',
                                    'max_length': 10,
                                    'value': 'value'
                                }
                            ]
                        }
                    ],
                    'information_fields': [
                        {
                            'information_field_type': 'TEXT_INFORMATION_FIELD',
                            'value': 'value'
                        },
                        {
                            'information_field_type': 'TEXT_INFORMATION_FIELD',
                            'value': 'value'
                        },
                    ]
                }
            ],
            'message': 'Formulários retornados com sucesso!'
        }

    def test_get_form_by_user_id_controller_no_requester_user(self):
        repo = FormRepositoryMock()
        usecase = GetFormByUserIdUsecase(repo)

        controller = GetFormByUserIdController(usecase)

        data = HttpRequest(body={})

        response = controller(data)

        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: requester_user'
    
    def test_get_form_by_user_id_controller_user_not_in_formularios_group(self):
        repo = FormRepositoryMock()
        usecase = GetFormByUserIdUsecase(repo)

        controller = GetFormByUserIdController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": '1',
                "name": 'Gabriel Godoy',
                "email": 'test@gmail.com',
                "cognito:groups": ""
            },   
        })

        response = controller(data)

        assert response.status_code == 403
        assert response.body == 'Ação não permitida: Usuário não esta apto para o sistema'

    def test_get_form_by_user_id_controller_no_items_found(self):
        repo = FormRepositoryMock()
        usecase = GetFormByUserIdUsecase(repo)

        controller = GetFormByUserIdController(usecase)
        repo.forms = []
        data = HttpRequest(body={"requester_user": {
                "sub": '1',
                "name": 'Gabriel Godoy',
                "email": 'test@gmail.com',
                "cognito:groups": "FORMULARIOS"
            },   
        })

        response = controller(data)

        assert response.status_code == 404
        assert response.body == 'Nenhum formulário encontrado'