import json

from src.modules.create_form.app.create_form_presenter import lambda_handler


class Test_CreateFormPresenter:
    def test_create_form_presenter(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/my/path",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "queryStringParameters": {
                "parameter1": "1"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                    "claims":
                        {
                            "sub": "d61dbf66-a10f-11ed-a8fc-0242ac120001",
                            "name": "Gabriel Godoy",
                            "email": "gabriel@gmail.com",
                            "cognito:groups": "FORMULARIOS"
                        }
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "external_interfaces": {
                    "method": "POST",
                    "path": "/my/path",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": {
                "form_title": "FORM TITLE",
                "user_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "can_vinculate": True,
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
                "justification": {
                    "options": [
                        {
                            "option": 'option',
                            "required_image": True,
                            "required_text": True
                        }
                    ],
                    "selected_option": 'option',
                    "text": 'text',
                    "image": 'image'
                },
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
                        "information_field_type": 'TEXT_INFORMATION_FIELD',
                        "value": 'value'
                    },
                    {
                        "information_field_type": 'TEXT_INFORMATION_FIELD',
                        "value": 'value'
                    }
                ]
            },
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        response_json = json.loads(response["body"])

        assert response["statusCode"] == 201
        assert response_json["message"] == "Formulário criado com sucesso!"
        assert response_json["form"]["form_id"] is not None
        assert response_json["form"]["status"] == "NOT_STARTED"
        assert response_json["form"]["form_title"] == "FORM TITLE"
        assert response_json["form"]["user_id"] == 'd61dbf66-a10f-11ed-a8fc-0242ac120001'
        assert response_json["form"]["can_vinculate"] == True
        assert response_json["form"]["template"] == 'TEMPLATE'
        assert response_json["form"]["area"] == '1'
        assert response_json["form"]["system"] == 'GAIA'
        assert response_json["form"]["street"] == '1'
        assert response_json["form"]["city"] == '1'
        assert response_json["form"]["number"] == 1
        assert response_json["form"]["latitude"] == 1.0
        assert response_json["form"]["longitude"] == 1.0
        assert response_json["form"]["region"] == 'REGION'
        assert response_json["form"]["priority"] == 'EMERGENCY'
        assert response_json["form"]["expiration_date"] == 946407600000
