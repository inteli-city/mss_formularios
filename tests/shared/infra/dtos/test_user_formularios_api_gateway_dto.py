import pytest
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.dtos.user_formularios_api_gateway_dto import UserFormulariosApiGatewayDTO


class Test_UserFormulariosApiGatewayDto:

    def test_user_api_gateway_dto_from_api_gateway(self):
        user_data = {
            'sub': 'd61dbf66-a10f-11ed-a8fc-0242ac120002',
            'name': 'Gabriel Godoy',
            'email': 'gabriel.godoy@gmail.com', 
            'cognito:groups': "GAIA,JUNDIAI,FORMULARIOS"
            }
        
        user_dto = UserFormulariosApiGatewayDTO.from_api_gateway(user_data)

        excepted_user_dto = UserFormulariosApiGatewayDTO(
            user_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
            name='Gabriel Godoy',
            email='gabriel.godoy@gmail.com',
            systems=['GAIA','JUNDIAI']
        )

        assert user_dto.user_id == excepted_user_dto.user_id
        assert user_dto.name == excepted_user_dto.name
        assert user_dto.email == excepted_user_dto.email
        assert user_dto.systems == ['GAIA','JUNDIAI']
    
    def test_user_api_gateway_dto_from_api_gateway_not_in_groups(self):
        user_data = {
            'sub': 'd61dbf66-a10f-11ed-a8fc-0242ac120002',
            'name': 'Gabriel Godoy',
            'email': 'gabriel.godoy@gmail.com', 
            'cognito:groups': "GAIA,JUNDIAI"
            }
        
        with pytest.raises(ForbiddenAction):
            UserFormulariosApiGatewayDTO.from_api_gateway(user_data)