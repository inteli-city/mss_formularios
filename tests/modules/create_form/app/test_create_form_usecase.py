from datetime import datetime

import pytest
from src.modules.create_form.app.create_form_usecase import CreateFormUsecase
from src.shared.domain.entities.field import TextField
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.enums.priority_enum import PRIORITY
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.form_repository_mock import FormRepositoryMock
from src.shared.infra.repositories.profile_repository_mock import ProfileRepositoryMock


class Test_CreateFormUsecase:

    def test_create_form_usecase(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()

        usecase = CreateFormUsecase(repo, repo_profile)

        text_field = TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='value')
        section = Section(section_id='99999', fields=[text_field, text_field])

        form = usecase(
            extern_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120020',
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
            description='123',
            priority=PRIORITY.EMERGENCY,
            expiration_date=946407600000,
            comments='123',
            sections=[
                section
            ],
            information_fields=repo.forms[0].information_fields
        )

        assert form.extern_form_id == 'd61dbf66-a10f-11ed-a8fc-0242ac120020'
        assert len(form.internal_form_id) == 36
        assert form.creator_user_id == 'd61dbf66-a10f-11ed-a8fc-0242ac120001'
        assert form.user_id == 'd61dbf66-a10f-11ed-a8fc-0242ac120001'
        assert form.coordinators_id == ['d61dbf66-a10f-11ed-a8fc-0242ac120001']
        assert form.vinculation_form_id == 'd61dbf66-a10f-11ed-a8fc-0242ac120010'
        assert form.template == 'TEMPLATE'
        assert form.area == '1'
        assert form.system == 'GAIA'
        assert form.street == '1'
        assert form.city == '1'
        assert form.number == 1
        assert form.latitude == 1.0
        assert form.longitude == 1.0
        assert form.region == 'REGION'
        assert form.description == '123'
        assert form.priority == PRIORITY.EMERGENCY
        assert form.status == FORM_STATUS.NOT_STARTED
        assert form.expiration_date == 946407600000
        assert form.creation_date == int(datetime.now().timestamp() * 1000)
        assert form.start_date == None
        assert form.conclusion_date == None
        assert form.justificative == None
        assert form.comments == '123'
        assert len(form.sections) == 1
        assert len(form.information_fields) == 2

    def test_create_form_usecase_creator_profile_none(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()

        usecase = CreateFormUsecase(repo, repo_profile)

        text_field = TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='value')
        section = Section(section_id='99999', fields=[text_field, text_field])

        with pytest.raises(ForbiddenAction):
            usecase(
                extern_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120020',
                creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120010',
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
                description='123',
                priority=PRIORITY.EMERGENCY,
                expiration_date=946407600000,
                comments='123',
                sections=[
                    section
                ],
                information_fields=repo.forms[0].information_fields
            )
    
    def test_create_form_usecase_creator_profile_not_enabled(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()

        usecase = CreateFormUsecase(repo, repo_profile)

        text_field = TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='value')
        section = Section(section_id='99999', fields=[text_field, text_field])

        with pytest.raises(ForbiddenAction):
            usecase(
                extern_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120020',
                creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120003',
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
                description='123',
                priority=PRIORITY.EMERGENCY,
                expiration_date=946407600000,
                comments='123',
                sections=[
                    section
                ],
                information_fields=repo.forms[0].information_fields
            )
    
    def test_create_form_usecase_creator_profile_not_in_system(self):
        repo = FormRepositoryMock()
        repo_profile = ProfileRepositoryMock()

        usecase = CreateFormUsecase(repo, repo_profile)

        text_field = TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='value')
        section = Section(section_id='99999', fields=[text_field, text_field])

        with pytest.raises(ForbiddenAction):
            usecase(
                extern_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120020',
                creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001',
                user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001',
                coordinators_id=['d61dbf66-a10f-11ed-a8fc-0242ac120001'],
                vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120010',
                template='TEMPLATE',
                area='1',
                system='123',
                street='1',
                city='1',
                number=1,
                latitude=1.0,
                longitude=1.0,
                region='REGION',
                description='123',
                priority=PRIORITY.EMERGENCY,
                expiration_date=946407600000,
                comments='123',
                sections=[
                    section
                ],
                information_fields=repo.forms[0].information_fields
            )