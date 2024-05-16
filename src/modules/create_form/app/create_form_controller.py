from src.modules.create_form.app.create_form_usecase import CreateFormUsecase
from src.shared.domain.enums.priority_enum import PRIORITY
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Conflict, Forbidden, InternalServerError, NotFound
from src.shared.infra.dtos.user_formularios_api_gateway_dto import UserFormulariosApiGatewayDTO


class CreateFormController:
    def __init__(self, usecase: CreateFormUsecase):
        self.CreateFormUsecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            
            requester_user = UserFormulariosApiGatewayDTO.from_api_gateway(request.data.get('requester_user'))

            if request.data.get('extern_form_id') is None:
                raise MissingParameters('extern_form_id')
            
            if request.data.get('user_id') is None:
                raise MissingParameters('user_id')
            
            if request.data.get('coordinators_id') is None:
                raise MissingParameters('coordinators_id')
            
            if request.data.get('template') is None:
                raise MissingParameters('template')
            
            if request.data.get('area') is None:
                raise MissingParameters('area')
            
            if request.data.get('system') is None:
                raise MissingParameters('system')
            
            if request.data.get('street') is None:
                raise MissingParameters('street')
            
            if request.data.get('city') is None:
                raise MissingParameters('city')
            
            if request.data.get('number') is None:
                raise MissingParameters('number')
            
            if request.data.get('latitude') is None:
                raise MissingParameters('latitude')
            
            if request.data.get('longitude') is None:
                raise MissingParameters('longitude')
            
            if request.data.get('region') is None:
                raise MissingParameters('region')
            
            if request.data.get('priority') is None:
                raise MissingParameters('priority')
            
            if request.data.get('expiration_date') is None:
                raise MissingParameters('expiration_date')
            
            if request.data.get('sections') is None:
                raise MissingParameters('sections')
            
            form = self.CreateFormUsecase(
                extern_form_id=request.data.get('extern_form_id'),
                creator_user_id=requester_user.user_id,
                user_id=request.data.get('user_id'),
                coordinators_id=request.data.get('coordinators_id'),
                vinculation_form_id=request.data.get('vinculation_form_id'),
                template=request.data.get('template'),
                area=request.data.get('area'),
                system=request.data.get('system'),
                street=request.data.get('street'),
                city=request.data.get('city'),
                number=request.data.get('number'),
                latitude=request.data.get('latitude'),
                longitude=request.data.get('longitude'),
                region=request.data.get('region'),
                description=request.data.get('description'),
                priority=PRIORITY[request.data.get('priority')],
                expiration_date=request.data.get('expiration_date'),
                comments=request.data.get('comments'),
                sections=[
                    {
                        'section_id': section.get('section_id'),
                        'fields': section.get('fields')
                    }
                    for section in request.data.get('sections')
                ],
                information_fields=request.data.get('information_fields')
            )
        
        except NoItemsFound as err:
            return NotFound(body=f'{err.message}')
        
        except DuplicatedItem as err:
            return Conflict(body=f'{err.message}')

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except ForbiddenAction as err:
            return Forbidden(body=err.message)
        
        except EntityError as err:
            return BadRequest(body=f"Parâmetro inválido: {err.message}")
        
        except Exception as err:
            return InternalServerError(body=err.args[0])