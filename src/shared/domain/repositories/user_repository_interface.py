from abc import ABC, abstractmethod
from typing import List, Tuple

from src.shared.domain.enums.role_enum import ROLE


class IUserRepository(ABC):

    @abstractmethod
    def get_groups_for_user(self, email: str) -> List[str]:
        pass
