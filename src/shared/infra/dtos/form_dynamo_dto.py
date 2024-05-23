from typing import List, Optional

from src.shared.domain.entities.form import Form
from src.shared.domain.entities.information_field import InformationField
from src.shared.domain.entities.justification import Justification
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.enums.priority_enum import PRIORITY
from src.shared.infra.dtos.section_dto import SectionDTO


class FormDynamoDTO:
    form_title: str
    form_id: str
    creator_user_id: str
    user_id: str
    vinculation_form_id: Optional[str]
    can_vinculate: bool
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
    justification: Justification
    comments: Optional[str]
    sections: List[Section]
    information_fields: Optional[List[InformationField]]

    def __init__(self, form_title: str, form_id: str, creator_user_id: str, user_id: str, vinculation_form_id: Optional[str], can_vinculate: bool, template: str, area: str, system: str, street: str, city: str, number: int, latitude: float, longitude: float, region: str, description: Optional[str], priority: PRIORITY, status: FORM_STATUS, expiration_date: int, creation_date: int, start_date: Optional[int], conclusion_date: Optional[int], justification: Justification, comments: Optional[str], sections: List[Section], information_fields: Optional[List[InformationField]]):
        self.form_title = form_title
        self.form_id = form_id
        self.creator_user_id = creator_user_id
        self.user_id = user_id
        self.vinculation_form_id = vinculation_form_id
        self.can_vinculate = can_vinculate
        self.template = template
        self.area = area
        self.system = system
        self.street = street
        self.city = city
        self.number = number
        self.latitude = latitude
        self.longitude = longitude
        self.region = region
        self.description = description
        self.priority = priority
        self.status = status
        self.expiration_date = expiration_date
        self.creation_date = creation_date
        self.start_date = start_date
        self.conclusion_date = conclusion_date
        self.justification = justification
        self.comments = comments
        self.sections = sections
        self.information_fields = information_fields


    @staticmethod
    def from_entity(form: Form) -> "FormDynamoDTO":
        return FormDynamoDTO(
            form_title=form.form_title,
            form_id=form.form_id,
            creator_user_id=form.creator_user_id,
            user_id=form.user_id,
            vinculation_form_id=form.vinculation_form_id,
            can_vinculate=form.can_vinculate,
            template=form.template,
            area=form.area,
            system=form.system,
            street=form.street,
            city=form.city,
            number=form.number,
            latitude=form.latitude,
            longitude=form.longitude,
            region=form.region,
            description=form.description,
            priority=form.priority,
            status=form.status,
            expiration_date=form.expiration_date,
            creation_date=form.creation_date,
            start_date=form.start_date,
            conclusion_date=form.conclusion_date,
            justification=form.justification,
            comments=form.comments,
            sections=form.sections,
            information_fields=form.information_fields
        )

    def to_dynamo(self) -> dict:
        return {
            'form_title': self.form_title,
            'form_id': self.form_id,
            'creator_user_id': self.creator_user_id,
            'user_id': self.user_id,
            'vinculation_form_id': self.vinculation_form_id,
            'can_vinculate': self.can_vinculate,
            'template': self.template,
            'area': self.area,
            'system': self.system,
            'street': self.street,
            'city': self.city,
            'number': self.number,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'region': self.region,
            'description': self.description,
            'priority': self.priority.value,
            'status': self.status.value,
            'expiration_date': self.expiration_date,
            'creation_date': self.creation_date,
            'start_date': self.start_date,
            'conclusion_date': self.conclusion_date,
            'justification': self.justification.to_dynamo(),
            'comments': self.comments,
            'sections': [
                SectionDTO
            ],
            'information_fields': [information_field.to_dynamo() for information_field in self.information_fields] if self.information_fields else None
        }