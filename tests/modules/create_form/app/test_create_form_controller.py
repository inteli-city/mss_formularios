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
    
    def test_create_form_controller_missing_request_user(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={
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

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: requester_user'
    
    def test_create_form_controller_missing_extern_form_id(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
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
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: extern_form_id'
    
    def test_create_form_controller_missing_user_id(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "extern_form_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120020',
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: user_id'
    
    def test_create_form_controller_missing_coordinators_id(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "extern_form_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120020',
            "user_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: coordinators_id'
    
    def test_create_form_controller_missing_template(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "extern_form_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120020',
            "user_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
            "coordinators_id": ['d61dbf66-a10f-11ed-a8fc-0242ac120001'],
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: template'
    
    def test_create_form_controller_missing_area(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "extern_form_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120020',
            "user_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
            "coordinators_id": ['d61dbf66-a10f-11ed-a8fc-0242ac120001'],
            "template": 'TEMPLATE',
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: area'
    
    def test_create_form_controller_missing_system(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "extern_form_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120020',
            "user_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
            "coordinators_id": ['d61dbf66-a10f-11ed-a8fc-0242ac120001'],
            "template": 'TEMPLATE',
            "area": '1',
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: system'
    
    def test_create_form_controller_missing_street(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "extern_form_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120020',
            "user_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
            "coordinators_id": ['d61dbf66-a10f-11ed-a8fc-0242ac120001'],
            "template": 'TEMPLATE',
            "area": '1',
            "system": 'GAIA',
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: street'
    
    def test_create_form_controller_missing_city(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
                "cognito:groups": "GAIA, JUNDIAI,FORMULARIOS"
            },
            "extern_form_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120020',
            "user_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
            "coordinators_id": ['d61dbf66-a10f-11ed-a8fc-0242ac120001'],
            "template": 'TEMPLATE',
            "area": '1',
            "system": 'GAIA',
            "street": '1',
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: city'
    
    def test_create_form_controller_missing_number(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: number'
    
    def test_create_form_controller_missing_latitude(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: latitude'
    
    def test_create_form_controller_missing_longitude(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: longitude'
    
    def test_create_form_controller_missing_region(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: region'
    
    def test_create_form_controller_missing_priority(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: priority'
    
    def test_create_form_controller_priority_not_in_enum(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={"requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
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
            "priority": 'EMERGENCIA',
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro inválido: priority'
    
    def test_create_form_controller_missing_expiration_date(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={
            "requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: expiration_date'
    
    def test_create_form_controller_missing_sections(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()
        usecase = CreateFormUsecase(repo, repo_profile)

        controller = CreateFormController(usecase)

        data = HttpRequest(body={
            "requester_user": {
                "sub": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "name": 'Gabriel Godoy',
                "email": repo_profile.profiles[0].email,
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
                }
            ]
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: sections'
    