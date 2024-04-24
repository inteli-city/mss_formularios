from typing import List

from src.shared.helpers.errors.usecase_errors import ForbiddenAction

class UserFormulariosApiGatewayDTO:
    user_id: str
    name: str
    email: str
    systems: List[str]

    def __init__(self, user_id: str, name: str, email: str, systems: List[str]):
        self.user_id = user_id

    @staticmethod
    def from_api_gateway(user_data: dict) -> 'UserFormulariosApiGatewayDTO':
        """
        This method is used to convert the user data from the API Gateway to a UserApiGatewayDTO object.
        """
        groups = [group.strip().upper() for group in user_data.get('cognito:groups', '').split(',') if group.strip()]

        if "FORMULARIOS" not in groups:
            raise ForbiddenAction('Usuário não esta apto para o sistema')

        return UserFormulariosApiGatewayDTO(
            user_id=user_data['sub'],
            name=user_data['name'],
            email=user_data['email'],
            systems=groups
        )
    
    def __eq__(self, other):
        return self.user_id == other.user_id