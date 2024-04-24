import abc
from typing import List, Optional

from src.shared.domain.entities.section import Section
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.enums.priority_enum import PRIORITY


class Form(abc.ABC):
    extern_form_id: str
    internal_form_id: str
    creator_user_id: str
    user_id: str
    coordinators_id: List[str]
    vinculation_form_id: Optional[str]
    template: str
    area: str
    system: str
    street: str
    city: str
    number: int
    latitude: float
    longitude: float
    region: str
    description: Optional[str]
    priority: PRIORITY
    status: FORM_STATUS
    expiration_date: int
    creation_date: int
    start_date: Optional[int]
    conclusion_date: Optional[int]
    justificative: Optional[str]
    comments: str
    sections: List[Section]

