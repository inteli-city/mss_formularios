from .login_profile_usecase import LoginProfileUsecase
from .login_profile_viewmodel import LoginProfileViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.infra.dtos.user_formularios_api_gateway_dto import UserFormulariosApiGatewayDTO
from src.shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError, OK, Forbidden
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class LoginProfileController:

    def __init__(self, usecase: LoginProfileUsecase):
        self.usecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserFormulariosApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))
        
            profile = self.usecase(
                requester_user_id=requester_user.user_id,
                name=requester_user.name,
                email=requester_user.email,
                systems=requester_user.systems
            )

            viewmodel = LoginProfileViewmodel(profile=profile)

            return OK(viewmodel.to_dict())

        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:
            return InternalServerError(body=err.args[0])