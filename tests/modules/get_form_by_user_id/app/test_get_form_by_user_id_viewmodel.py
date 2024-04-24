from src.modules.get_form_by_user_id.app.get_form_by_user_id_viewmodel import FieldViewmodel, FormViewmodel, GetFormByUserIdViewmodel, SectionViewmodel
from src.shared.domain.entities.field import FileField, TextField
from src.shared.domain.entities.form import Form
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.file_type_enum import FILE_TYPE
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.enums.priority_enum import PRIORITY


class Test_GetFormByUserIdViewmodel:

    def test_field_viewmodel(self):
        viewmodel = FieldViewmodel(field=TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='value'))

        respose = viewmodel.to_dict()

        excepted = {
            'field_type': 'TEXT_FIELD',
            'placeholder': 'placeholder',
            'required': True,
            'key': 'key',
            'regex': 'regex',
            'formatting': 'formatting',
            'max_length': 10,
            'value': 'value'
        }

        assert respose == excepted
    
    def test_field_viewmodel_with_enum(self):
        viewmodel = FieldViewmodel(field=FileField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', file_type=FILE_TYPE.IMAGE, min_quantity=1, max_quantity=10, value=['value']))

        respose = viewmodel.to_dict()

        excepted = {
            'field_type': 'FILE_FIELD',
            'placeholder': 'placeholder',
            'required': True,
            'key': 'key',
            'regex': 'regex',
            'formatting': 'formatting',
            'file_type': 'IMAGE',
            'min_quantity': 1,
            'max_quantity': 10,
            'value': ['value']
        }

        assert respose == excepted
    
    def test_field_viewmodel_with_none(self):
        viewmodel = FieldViewmodel(field=TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=None, value=None))

        respose = viewmodel.to_dict()

        excepted = {
            'field_type': 'TEXT_FIELD',
            'placeholder': 'placeholder',
            'required': True,
            'key': 'key',
            'regex': 'regex',
            'formatting': 'formatting',
            'max_length': None,
            'value': None
        }

        assert respose == excepted
    
    def test_section_viewmodel(self):

        field = FileField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', file_type=FILE_TYPE.IMAGE, min_quantity=1, max_quantity=10, value=['value'])

        viewmodel = SectionViewmodel(
            section=Section(
                section_id='section_id',
                fields=[field]
            )
        )

        respose = viewmodel.to_dict()

        excepted = {
            'section_id': 'section_id',
            'fields': [{
                'field_type': 'FILE_FIELD',
                'placeholder': 'placeholder',
                'required': True,
                'key': 'key',
                'regex': 'regex',
                'formatting': 'formatting',
                'file_type': 'IMAGE',
                'min_quantity': 1,
                'max_quantity': 10,
                'value': ['value']
            }]
        }

        assert respose == excepted
    
    def test_form_viewmodel(self):
        field = FileField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', file_type=FILE_TYPE.IMAGE, min_quantity=1, max_quantity=10, value=['value'])

        section = Section(
                section_id='section_id',
                fields=[field]
            )
        
        viewmodel = FormViewmodel(
            form=Form(
                extern_form_id='extern_form_id',
                internal_form_id='internal_form_id',
                creator_user_id='creator_user_id',
                user_id='user_id',
                coordinators_id=['coordinators_id'],
                vinculation_form_id='vinculation_form_id',
                template='template',
                area='area',
                system='system',
                street='street',
                city='city',
                number=1,
                latitude=1.0,
                longitude=1.0,
                region='region',
                description='description',
                priority=PRIORITY.HIGH,
                status=FORM_STATUS.IN_PROGRESS,
                expiration_date=1,
                creation_date=1,
                start_date=1,
                conclusion_date=1,
                justificative='justificative',
                comments='comments',
                sections=[section]
            )
        )

        respose = viewmodel.to_dict()

        excepted = {
            'extern_form_id': 'extern_form_id',
            'internal_form_id': 'internal_form_id',
            'creator_user_id': 'creator_user_id',
            'user_id': 'user_id',
            'coordinators_id': ['coordinators_id'],
            'vinculation_form_id': 'vinculation_form_id',
            'template': 'template',
            'area': 'area',
            'system': 'system',
            'street': 'street',
            'city': 'city',
            'number': 1,
            'latitude': 1.0,
            'longitude': 1.0,
            'region': 'region',
            'description': 'description',
            'priority': 'HIGH',
            'status': 'IN_PROGRESS',
            'expiration_date': 1,
            'creation_date': 1,
            'start_date': 1,
            'conclusion_date': 1,
            'justificative': 'justificative',
            'comments': 'comments',
            'sections': [{
                'section_id': 'section_id',
                'fields': [{
                    'field_type': 'FILE_FIELD',
                    'placeholder': 'placeholder',
                    'required': True,
                    'key': 'key',
                    'regex': 'regex',
                    'formatting': 'formatting',
                    'file_type': 'IMAGE',
                    'min_quantity': 1,
                    'max_quantity': 10,
                    'value': ['value']
                }]
            }]
        }

        assert respose == excepted
    
    def test_get_form_by_user_id_viewmodel(self):
        field = FileField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', file_type=FILE_TYPE.IMAGE, min_quantity=1, max_quantity=10, value=['value'])

        section = Section(
                section_id='section_id',
                fields=[field]
            )
        
        form = Form(
                extern_form_id='extern_form_id',
                internal_form_id='internal_form_id',
                creator_user_id='creator_user_id',
                user_id='user_id',
                coordinators_id=['coordinators_id'],
                vinculation_form_id='vinculation_form_id',
                template='template',
                area='area',
                system='system',
                street='street',
                city='city',
                number=1,
                latitude=1.0,
                longitude=1.0,
                region='region',
                description='description',
                priority=PRIORITY.HIGH,
                status=FORM_STATUS.IN_PROGRESS,
                expiration_date=1,
                creation_date=1,
                start_date=1,
                conclusion_date=1,
                justificative='justificative',
                comments='comments',
                sections=[section]
            )

        viewmodel = GetFormByUserIdViewmodel(
            form_list=[form]
        )

        respose = viewmodel.to_dict()

        excepted = {
            'form_list': [
                {
                    'extern_form_id': 'extern_form_id',
                    'internal_form_id': 'internal_form_id',
                    'creator_user_id': 'creator_user_id',
                    'user_id': 'user_id',
                    'coordinators_id': ['coordinators_id'],
                    'vinculation_form_id': 'vinculation_form_id',
                    'template': 'template',
                    'area': 'area',
                    'system': 'system',
                    'street': 'street',
                    'city': 'city',
                    'number': 1,
                    'latitude': 1.0,
                    'longitude': 1.0,
                    'region': 'region',
                    'description': 'description',
                    'priority': 'HIGH',
                    'status': 'IN_PROGRESS',
                    'expiration_date': 1,
                    'creation_date': 1,
                    'start_date': 1,
                    'conclusion_date': 1,
                    'justificative': 'justificative',
                    'comments': 'comments',
                    'sections': [
                        {
                            'section_id': 'section_id',
                            'fields': [
                                {
                                    'field_type': 'FILE_FIELD',
                                    'placeholder': 'placeholder',
                                    'required': True,
                                    'key': 'key',
                                    'regex': 'regex',
                                    'formatting': 'formatting',
                                    'file_type': 'IMAGE',
                                    'min_quantity': 1,
                                    'max_quantity': 10,
                                    'value': ['value']
                                }
                            ]
                        }
                    ]
                }
            ],
            'message': 'Formulários retornados com sucesso!'
        }