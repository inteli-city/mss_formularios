import json
from src.modules.cancel_form.app.cancel_form_presenter import lambda_handler


class Test_CancelFormPresenter:

    def test_cancel_form_presenter(self):
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
                "form_id": "d61dbf66-a10f-11ed-a8fc-0242ac120010",
                "selected_option": "option",
                "justification_text": "justification_test",
                "justification_image": "image_test"
            },
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        response_json = json.loads(response["body"])

        assert response["statusCode"] == 200
        assert response_json['message'] == 'Formulário cancelado com sucesso!'
        assert response_json['form']['form_id'] == 'd61dbf66-a10f-11ed-a8fc-0242ac120010'
        assert response_json['form']['status'] == 'CANCELED'
        assert response_json['form']['justification']['justification_text'] == 'justification_test'
        assert response_json['form']['justification']['justification_image'].startswith('https://test')