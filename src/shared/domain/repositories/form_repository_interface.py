from abc import ABC, abstractmethod
from typing import List

from src.shared.domain.entities.form import Form
from src.shared.domain.enums.form_status_enum import FORM_STATUS


class IFormRepository(ABC):
    
    @abstractmethod
    def get_form_by_user_id(self, user_id: str) -> List[Form]:
        pass

    @abstractmethod
    def create_form(self, form: Form) -> Form:
        pass

    @abstractmethod
    def update_form_status(self, form_id: str, status: FORM_STATUS) -> Form:
        pass