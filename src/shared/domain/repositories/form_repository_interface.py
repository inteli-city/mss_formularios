from abc import ABC, abstractmethod
from typing import List

from src.shared.domain.entities.form import Form


class IFormRepository(ABC):
    
    @abstractmethod
    def get_form_by_user_id(self, user_id: str) -> List[Form]:
        pass

    @abstractmethod
    def create_form(self, form: Form) -> Form:
        pass