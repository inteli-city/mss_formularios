from datetime import datetime, timedelta
from typing import List
from src.shared.domain.entities.field import TextField
from src.shared.domain.entities.form import Form
from src.shared.domain.entities.information_field import TextInformationField
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.enums.priority_enum import PRIORITY
from src.shared.domain.repositories.form_repository_interface import IFormRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem


class FormRepositoryMock(IFormRepository):
    forms: List[Form]

    def __init__(self):
        def timestamp_yesterday():
            current_date = datetime.now()
            yesterday_date = current_date - timedelta(days=1)

            timestamp_yesterday_seconds = int(yesterday_date.timestamp())
            timestamp_yesterday_milliseconds = timestamp_yesterday_seconds * 1000
            return timestamp_yesterday_milliseconds

        text_field = TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='value')
        section = Section(section_id='99999', fields=[text_field, text_field])
        information_field = TextInformationField(
            value='value'
        )

        self.forms = [
            Form(
                extern_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120010',
                internal_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120010',
                creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001',
                user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001',
                coordinators_id=['d61dbf66-a10f-11ed-a8fc-0242ac120001'],
                vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120010',
                template='TEMPLATE',
                area='1',
                system='GAIA',
                street='1',
                city='1',
                number=1,
                latitude=1.0,
                longitude=1.0,
                region='REGION',
                description=None,
                priority=PRIORITY.EMERGENCY,
                status=FORM_STATUS.CONCLUDED,
                expiration_date=946407600000,
                creation_date=946407600000,
                start_date=946407600000,
                conclusion_date=timestamp_yesterday(),
                justificative=None,
                comments=None,
                sections=[section, section],
                information_fields=[
                    information_field,
                    information_field,
                ]
            ),
            Form(
                extern_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120011',
                internal_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120011',
                creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001',
                user_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                coordinators_id=['d61dbf66-a10f-11ed-a8fc-0242ac120011'],
                vinculation_form_id=None,
                template='TEMPLATE',
                area='1',
                system='GAIA',
                street='1',
                city='1',
                number=1,
                latitude=1.0,
                longitude=1.0,
                region='REGION',
                description=None,
                priority=PRIORITY.EMERGENCY,
                status=FORM_STATUS.CONCLUDED,
                expiration_date=946407600000,
                creation_date=946407600000,
                start_date=946407600000,
                conclusion_date=946407600000,
                justificative=None,
                comments=None,
                sections=[section],
                information_fields=[
                    information_field,
                    information_field,
                ]
            ),
        ]
    
    def get_form_by_user_id(self, user_id: str) -> List[Form]:
        current_date = datetime.now()


        filtered_forms = []
        for form in self.forms:
            if form.user_id == user_id:
                filtered_forms.append(form)

        return filtered_forms
    
    def create_form(self, form: Form) -> Form:
        for item in self.forms:
            if form.extern_form_id == item.extern_form_id:
                raise DuplicatedItem('Formulário já existe')
        self.forms.append(form)
        return form