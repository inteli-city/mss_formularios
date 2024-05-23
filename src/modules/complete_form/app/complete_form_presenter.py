from src.modules.complete_form.app.complete_form_controller import CompleteFormController
from src.modules.complete_form.app.complete_form_usecase import CompleteFormUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo = Environments.get_form_repo()()
repo_profile = Environments.get_profile_repo()()
usecase = CompleteFormUsecase(repo, repo_profile)
controller = CompleteFormController(usecase)

def lambda_handler(event, context):
    
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    
    return httpResponse.toDict()