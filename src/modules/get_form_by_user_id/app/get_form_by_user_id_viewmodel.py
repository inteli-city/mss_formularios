from enum import Enum
from typing import List, Optional

from src.shared.domain.entities.field import Field
from src.shared.domain.entities.form import Form
from src.shared.domain.entities.information_field import InformationField
from src.shared.domain.entities.justificative import Justificative, JustificativeOption
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
 
class JustificativeOptionViewmodel:
    option: str
    requiredImage: bool
    requiredText: bool

    def __init__(self, justificative_option: JustificativeOption):
        self.option = justificative_option.option
        self.requiredImage = justificative_option.requiredImage
        self.requiredText = justificative_option.requiredText

    def to_dict(self):
        return {
            'option': self.option,
            'requiredImage': self.requiredImage,
            'requiredText': self.requiredText
        }

class JustificativeViewmodel:
    options: List[JustificativeOptionViewmodel]
    selectedOption: Optional[str]
    text: Optional[str]
    image: Optional[str]

    def __init__(self, justificative: Justificative):
        self.options = [JustificativeOptionViewmodel(option).to_dict() for option in justificative.options]
        self.selectedOption = justificative.selectedOption
        self.text = justificative.text
        self.image = justificative.image

    def to_dict(self):
        return {
            'options': self.options,
            'selectedOption': self.selectedOption,
            'text': self.text,
            'image': self.image
        }

class FormViewmodel:
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
    justificative: Justificative
    comments: Optional[str]
    sections: List[Section]
    information_fields: Optional[List[InformationField]]

    def __init__(self, form: Form):
        self.form_title = form.form_title
        self.form_id = form.form_id
        self.creator_user_id = form.creator_user_id
        self.user_id = form.user_id
        self.vinculation_form_id = form.vinculation_form_id
        self.can_vinculate = form.can_vinculate
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
            'justificative': JustificativeViewmodel(self.justificative).to_dict(),
            'comments': self.comments,
            'sections': [SectionViewmodel(section).to_dict() for section in self.sections],
            'information_fields': [InformationFieldViewmodel(information_field).to_dict() for information_field in self.information_fields] if self.information_fields is not None else None
        }
    
class GetFormByUserIdViewmodel:
    form_list: List[Form]

    def __init__(self, form_list: List[Form]):
        self.form_list = form_list
    
    def to_dict(self):
        return {
            'form_list': [FormViewmodel(form).to_dict() for form in self.form_list],
            'message': 'Formulários retornados com sucesso!'
        }