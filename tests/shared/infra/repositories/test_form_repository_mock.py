import pytest
from src.shared.domain.entities.field import TextField
from src.shared.domain.entities.form import Form
from src.shared.domain.entities.information_field import TextInformationField
from src.shared.domain.entities.justificative import Justificative, JustificativeOption
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.enums.priority_enum import PRIORITY
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.infra.repositories.form_repository_mock import FormRepositoryMock

justificative_option = JustificativeOption(
    option='option',
    requiredImage=True,
    requiredText=True
)

justificative = Justificative(
    options=[justificative_option],
    selectedOption='selectedOption',
    text='text',
    image='image'
)

class Test_FormRepositoryMock:

    def test_form_repository_mock_get_form_by_user_id(self):
        repo = FormRepositoryMock()
        form = repo.get_form_by_user_id(repo.forms[0].user_id)

        assert len(form) == 1

    def test_form_repository_mock_create_form(self):
        repo = FormRepositoryMock()
        text_field = TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='value')
        section = Section(section_id='99999', fields=[text_field, text_field])
        information_field = TextInformationField(
            value='value'
        )
        form_to_create = Form(
                form_title='FORM TITLE',
                form_id='d61dbf66-a10f-11ed-a8fc-0242ac120012',
                creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001',
                user_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                vinculation_form_id=None,
                can_vinculate=True,
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
                justificative=justificative,
                comments=None,
                sections=[section],
                information_fields=[
                    information_field,
                    information_field,
                ]
        )

        form = repo.create_form(
            form=form_to_create
        )

        assert form.form_id == 'd61dbf66-a10f-11ed-a8fc-0242ac120012'

    def test_form_repository_mock_create_form_duplicated_form_id(self):
        repo = FormRepositoryMock()
        with pytest.raises(DuplicatedItem):
            repo.create_form(repo.forms[0])