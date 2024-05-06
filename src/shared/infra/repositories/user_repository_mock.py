from typing import List, Tuple

from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class UserRepositoryMock(IUserRepository):
    users: List[Tuple[str, List[str]]]

    def __init__(self):
        self.users = [
            ('gabriel@gmail.com', ['GAIA', 'FORMULARIOS', 'JUNDIAI']),
            ('gabriel@hotmail.com', ['GAIA', 'FORMULARIOS', 'JUNDIAI']),
            ('gabriel@outlook.com', ['GAIA', 'JUNDIAI']),
        ]
    
    def get_groups_for_user(self, email: str) -> List[str]:
        for user in self.users:
            if user[0] == email:
                return user[1]
        raise NoItemsFound('Usuário não encontrado')