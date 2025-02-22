from .create_form_controller import CreateFormController
from .create_form_usecase import CreateFormUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo = Environments.get_form_repo()()
image_repo = Environments.get_image_repo()()
repo_profile = Environments.get_profile_repo()()
usecase = CreateFormUsecase(repo, repo_profile, image_repo)
controller = CreateFormController(usecase)

def lambda_handler(event, context):
    
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    
    return httpResponse.toDict()