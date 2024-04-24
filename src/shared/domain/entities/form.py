import abc
from typing import List, Optional

from src.shared.domain.entities.information_field import InformationField
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.enums.priority_enum import PRIORITY
from src.shared.helpers.errors.domain_errors import EntityError


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
    comments: Optional[str]
    sections: List[Section]
    information_fields: Optional[List[InformationField]]

    def __init__(self, extern_form_id: str, internal_form_id: str, creator_user_id: str, user_id: str, coordinators_id: List[str], vinculation_form_id: Optional[str], template: str, area: str, system: str, street: str, city: str, number: int, latitude: float, longitude: float, region: str, description: Optional[str], priority: PRIORITY, status: FORM_STATUS, expiration_date: int, creation_date: int, start_date: Optional[int], conclusion_date: Optional[int], justificative: Optional[str], comments: Optional[str], sections: List[Section], information_fields: Optional[List[InformationField]] = None):

        if type(extern_form_id) is not str:
            raise EntityError('extern_form_id')
        self.extern_form_id = extern_form_id

        if type(internal_form_id) is not str:
            raise EntityError('internal_form_id')
        self.internal_form_id = internal_form_id

        if type(creator_user_id) is not str:
            raise EntityError('creator_user_id')
        self.creator_user_id = creator_user_id

        if type(user_id) is not str:
            raise EntityError('user_id')
        self.user_id = user_id

        if not isinstance(coordinators_id, list):
            raise EntityError('coordinators_id')
        if not coordinators_id:
            raise EntityError('coordinators_id')
        if not all(isinstance(coordinator_id, str) for coordinator_id in coordinators_id):
            raise EntityError('coordinators_id')
        self.coordinators_id = coordinators_id

        if vinculation_form_id is not None and type(vinculation_form_id) is not str:
            raise EntityError('vinculation_form_id')
        self.vinculation_form_id = vinculation_form_id

        if type(template) is not str:
            raise EntityError('template')
        self.template = template

        if type(area) is not str:
            raise EntityError('area')
        self.area = area

        if type(system) is not str:
            raise EntityError('system')
        self.system = system

        if type(street) is not str:
            raise EntityError('street')
        self.street = street

        if type(city) is not str:
            raise EntityError('city')
        self.city = city

        if type(number) is not int:
            raise EntityError('number')
        self.number = number

        if type(latitude) is not float:
            raise EntityError('latitude')
        self.latitude = latitude

        if type(longitude) is not float:
            raise EntityError('longitude')
        self.longitude = longitude

        if type(region) is not str:
            raise EntityError('region')
        self.region = region

        if description is not None and type(description) is not str:
            raise EntityError('description')
        self.description = description

        if type(priority) is not PRIORITY:
            raise EntityError('priority')
        self.priority = priority

        if type(status) is not FORM_STATUS:
            raise EntityError('status')
        self.status = status

        if type(expiration_date) is not int:
            raise EntityError('expiration_date')
        self.expiration_date = expiration_date

        if type(creation_date) is not int:
            raise EntityError('creation_date')
        self.creation_date = creation_date

        if start_date is not None and type(start_date) is not int:
            raise EntityError('start_date')
        if status == FORM_STATUS.IN_PROGRESS and start_date is None:
            raise EntityError('start_date')
        self.start_date = start_date

        if conclusion_date is not None and type(conclusion_date) is not int:
            raise EntityError('conclusion_date')
        if status == FORM_STATUS.CONCLUDED and conclusion_date is None:
            raise EntityError('conclusion_date')
        self.conclusion_date = conclusion_date

        if justificative is not None and type(justificative) is not str:
            raise EntityError('justificative')
        self.justificative = justificative

        if comments is not None and type(comments) is not str:
            raise EntityError('comments')
        self.comments = comments

        if not isinstance(sections, list):
            raise EntityError('sections')
        if not sections:
            raise EntityError('sections')
        if not all(isinstance(section, Section) for section in sections):
            raise EntityError('sections')
        self.sections = sections

        if information_fields is not None:
            if not isinstance(information_fields, list):
                raise EntityError('information_fields')
            if not information_fields:
                raise EntityError('information_fields')
            if not all(isinstance(information_field, InformationField) for information_field in information_fields):
                raise EntityError('information_fields')
    