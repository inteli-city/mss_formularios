import pytest
from src.shared.domain.entities.field import TextField
from src.shared.domain.entities.form import Form
from src.shared.domain.entities.information_field import TextInformationField
from src.shared.domain.entities.justification import Justification, JustificationOption
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.fields_enum import FIELD_TYPE
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.enums.priority_enum import PRIORITY
from src.shared.infra.repositories.form_repository_dynamo import FormRepositoryDynamo


class Test_FormRepositoryDynamo:

    @pytest.mark.skip("Can't run test in github actions")
    def test_form_repository_dynamo_create_form(self):
        repo = FormRepositoryDynamo()

        form_to_create = Form(
            form_title='form_title',
            form_id='d61dbf66-a10f-11ed-a8fc-0242ac120010',
            creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120010',
            user_id='125fb34e-aacf-4a47-9914-82ea64ff9f32',
            vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120010',
            can_vinculate=True,
            template='template',
            area='area',
            system='system',
            street='street',
            city='city',
            number=123,
            latitude=0.0,
            longitude=0.0,
            region='region',
            description='description',
            priority=PRIORITY.EMERGENCY,
            status=FORM_STATUS.IN_PROGRESS,
            expiration_date=12345678,
            creation_date=12345678,
            start_date=12345678,
            conclusion_date=12345678,
            justification=Justification(
                options=[
                    JustificationOption(
                        option='option',
                        required_image=True,
                        required_text=True
                    )
                ],
                selected_option='selected_option',
                justification_text='justification_text',
                justification_image='justification_image'
            ),
            comments='comments',
            sections=[
                Section(
                    section_id='0',
                    fields=[
                        TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='poggers')
                    ]
                )
            ],
            information_fields=[
                TextInformationField(
                    value='value'
                )
            ]
        )

        form = repo.create_form(form=form_to_create)

        assert form is not None

    @pytest.mark.skip("Can't run test in github actions")
    def test_form_repository_dynamo_get_form_by_user_id(self):
        repo = FormRepositoryDynamo()

        forms = repo.get_form_by_user_id(user_id='125fb34e-aacf-4a47-9914-82ea64ff9f32')

        assert len(forms) == 1
        assert isinstance(forms[0], Form)
        assert forms[0].form_id == 'd61dbf66-a10f-11ed-a8fc-0242ac120010'

