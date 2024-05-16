from enum import Enum
from typing import List, Optional

from src.shared.domain.entities.field import Field
from src.shared.domain.entities.form import Form
from src.shared.domain.entities.information_field import InformationField
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.fields_enum import FIELD_TYPE
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.enums.priority_enum import PRIORITY


class FieldViewmodel:
    field: Field

    def __init__(self, field: Field):
        self.field = field
    
    def to_dict(self):
        return {attr: getattr(self.field, attr).value if isinstance(getattr(self.field, attr), Enum) else getattr(self.field, attr) for attr in vars(self.field)}

class InformationFieldViewmodel:
    information_field: InformationField

    def __init__(self, information_field: Field):
        self.information_field = information_field
    
    def to_dict(self):
        return {attr: getattr(self.information_field, attr).value if isinstance(getattr(self.information_field, attr), Enum) else getattr(self.information_field, attr) for attr in vars(self.information_field)}

class SectionViewmodel:
    section_id: str
    fields: List[Field]

    def __init__(self, section: Section):
        self.section_id = section.section_id
        self.fields = section.fields
    
    def to_dict(self):
        return {
            'section_id': self.section_id,
            'fields': [FieldViewmodel(field).to_dict() for field in self.fields]
        }

class FormViewmodel:
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
    comments: Optional[str]
    sections: List[Section]
    information_fields: Optional[List[InformationField]]

    def __init__(self, form: Form):
        self.extern_form_id = form.extern_form_id
        self.internal_form_id = form.internal_form_id
        self.creator_user_id = form.creator_user_id
        self.user_id = form.user_id
        self.coordinators_id = form.coordinators_id
        self.vinculation_form_id = form.vinculation_form_id
        self.template = form.template
        self.area = form.area
        self.system = form.system
        self.street = form.street
        self.city = form.city
        self.number = form.number
        self.latitude = form.latitude
        self.longitude = form.longitude
        self.region = form.region
        self.description = form.description
        self.priority = form.priority
        self.status = form.status
        self.expiration_date = form.expiration_date
        self.creation_date = form.creation_date
        self.start_date = form.start_date
        self.conclusion_date = form.conclusion_date
        self.justificative = form.justificative
        self.comments = form.comments
        self.sections = form.sections
        self.information_fields = form.information_fields

    def to_dict(self):
        return {
            'extern_form_id': self.extern_form_id,
            'internal_form_id': self.internal_form_id,
            'creator_user_id': self.creator_user_id,
            'user_id': self.user_id,
            'coordinators_id': self.coordinators_id,
            'vinculation_form_id': self.vinculation_form_id,
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
            'justificative': self.justificative,
            'comments': self.comments,
            'sections': [SectionViewmodel(section).to_dict() for section in self.sections],
            'information_fields': [InformationFieldViewmodel(information_field).to_dict() for information_field in self.information_fields]
        }
    
class CreateFormViewmodel:
    form: Form

    def __init__(self, form: Form):
        self.form = form
    
    def to_dict(self):
        return {
            'form': FormViewmodel(self.form).to_dict(),
            'message': 'Formulários retornados com sucesso!'
        }