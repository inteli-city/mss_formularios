

import pytest
from src.shared.domain.entities.field import TextField
from src.shared.domain.entities.form import Form
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.enums.priority_enum import PRIORITY
from src.shared.helpers.errors.domain_errors import EntityError


text_field = TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='value')
section = Section(section_id='99999', fields=[text_field, text_field])
class Test_Form:

    def test_form(self):
        Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_extern_form_id_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id=99999, internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_internal_form_id_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id=99999, creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_creator_user_id_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id=99999, user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_user_id_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id=99999, coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_coordinators_id_not_list(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id='99999', vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_coordinators_id_is_empty(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=[], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_coordinators_id_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=[99999], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_vinculation_form_id_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id=99999, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_template_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template=99999, area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_area_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area=99999, system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_system_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system=99999, street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_street_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street=99999, city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_city_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city=99999, number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_number_not_int(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number='99999', latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_latitude_not_float(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude='99999.99', longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_longitude_not_float(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude='99999.99', region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_region_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region=99999, description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_description_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description=99999, priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_priority_not_enum(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority='PRIORITY.EMERGENCY', status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=None, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_status_not_enum(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status='FORM_STATUS.IN_PROGRESS', expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=None, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_expiration_date_not_int(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date='946407600000', creation_date=946407600000, start_date=None, conclusion_date=None, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_expiration_date_not_timestamp(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=123, creation_date=946407600000, start_date=None, conclusion_date=None, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_creation_date_not_int(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date='946407600000', start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_creation_date_not_timestamp(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=123, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_start_date_not_int(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date='946407600000', conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_start_date_not_timestamp(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=123, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_start_date_status_in_progress_not_none(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=None, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[section, section])

    def test_conclusion_date_not_int(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date='946407600000', justificative='justificative', comments='comments', sections=[section, section])
    
    def test_conclusion_date_not_timestamp(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=123, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_conclusion_date_status_concluded_not_none(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.CONCLUDED, expiration_date=946407600000, creation_date=946407600000, start_date=None, conclusion_date=None, justificative='justificative', comments='comments', sections=[section, section])
    
    def test_justificative_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=99999, comments='comments', sections=[section, section])
    
    def test_comments_not_str(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments=99999, sections=[section, section])
    
    def test_sections_not_list(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=section)
    
    def test_sections_is_empty(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=[])
    
    def test_sections_not_section(self):
        with pytest.raises(EntityError):
            Form(extern_form_id='99999', internal_form_id='99999', creator_user_id='99999', user_id='99999', coordinators_id=['99999'], vinculation_form_id='99999', template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative='justificative', comments='comments', sections=['section', 'section'])