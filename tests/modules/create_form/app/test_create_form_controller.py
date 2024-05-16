from src.modules.create_form.app.create_form_controller import CreateFormController
from src.modules.create_form.app.create_form_usecase import CreateFormUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.form_repository_mock import FormRepositoryMock
from src.shared.infra.repositories.profile_repository_mock import ProfileRepositoryMock


class Test_CreateFormController:
    def test_create_form_controller(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": 'gabriel@gmail.com',
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "extern_form_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120020',
            "user_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
            "coordinators_id": ['d61dbf66-a10f-11ed-a8fc-0242ac120001'],
            "template": 'TEMPLATE',
            "area": '1',
            "system": 'GAIA',
            "street": '1',
            "city": '1',
            "number": 1,
            "latitude": 1.0,
            "longitude": 1.0,
            "region": 'REGION',
            "priority": 'EMERGENCY',
            "expiration_date": 946407600000,
            "comments": '123',
            "sections": [
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
            ],
            "information_fields": [
                {
                    "field_type": 'TEXT_FIELD',
                    "placeholder": 'placeholder',
                    "required": True,
                    "key": 'key',
                    "regex": 'regex',
                    "formatting": 'formatting',
                    "max_length": 10,
                    "value": 'value'
                },
                {
                    "field_type": 'TEXT_FIELD',
                    "placeholder": 'placeholder',
                    "required": True,
                    "key": 'key',
                    "regex": 'regex',
                    "formatting": 'formatting',
                    "max_length": 10,
                    "value": 'value'
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 201
        assert response.body['message'] == 'Formulário criado com sucesso!'