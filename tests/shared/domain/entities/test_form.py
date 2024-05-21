import pytest
from src.shared.domain.entities.field import TextField
from src.shared.domain.entities.form import Form
from src.shared.domain.entities.information_field import TextInformationField
from src.shared.domain.entities.justificative import Justificative, JustificativeOption
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.enums.priority_enum import PRIORITY
from src.shared.helpers.errors.domain_errors import EntityError


text_field = TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='value')
section = Section(section_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', fields=[text_field, text_field])
information_field = TextInformationField(value='value')
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
class Test_Form:

    def test_form(self):
        Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])
    
    def test_form_title_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title=99999, form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])

    def test_form_id_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id=99999, creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=None)
    
    def test_creator_user_id_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id=99999, user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])
    
    def test_user_id_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id=99999, vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])
        
    def test_vinculation_form_id_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id=99999, can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])
    
    def test_can_vinculate_not_bool(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=99999, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])

    def test_template_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template=99999, area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])
    
    def test_area_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area=99999, system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])
    
    def test_system_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system=99999, street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])
    
    def test_street_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street=99999, city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])
    
    def test_city_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city=99999, number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])
    
    def test_number_not_int(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number='d61dbf66-a10f-11ed-a8fc-0242ac120001', latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])
    
    def test_latitude_not_float(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude='99999.99', longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])
    
    def test_longitude_not_float(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude='99999.99', region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[information_field, information_field])
    
    def test_region_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region=99999, description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=None)
    
    def test_description_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description=99999, priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=None)
    
    def test_priority_not_enum(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority='PRIORITY.EMERGENCY', status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=None, justificative=justificative, comments='comments', sections=[section, section], information_fields=None)
    
    def test_status_not_enum(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status='FORM_STATUS.IN_PROGRESS', expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=None, justificative=justificative, comments='comments', sections=[section, section], information_fields=None)
    
    def test_expiration_date_not_int(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date='946407600000', creation_date=946407600000, start_date=None, conclusion_date=None, justificative=justificative, comments='comments', sections=[section, section], information_fields=None)
    
    def test_creation_date_not_int(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date='946407600000', start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=None)
    
    def test_start_date_not_int(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date='946407600000', conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=None)
    
    def test_start_date_status_in_progress_not_none(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=None, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=None)

    def test_conclusion_date_not_int(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date='946407600000', justificative=justificative, comments='comments', sections=[section, section], information_fields=None)
    
    def test_conclusion_date_status_concluded_not_none(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.CONCLUDED, expiration_date=946407600000, creation_date=946407600000, start_date=None, conclusion_date=None, justificative=justificative, comments='comments', sections=[section, section], information_fields=None)
    
    def test_justificative_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=99999, comments='comments', sections=[section, section], information_fields=None)
    
    def test_comments_not_str(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments=99999, sections=[section, section], information_fields=None)
    
    def test_sections_not_list(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=section, information_fields=None)
    
    def test_sections_is_empty(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[], information_fields=None)
    
    def test_sections_not_section(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=['section', 'section'], information_fields=None)
    
    def test_information_fields_not_list(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=information_field)
    
    def test_information_fields_is_empty(self):
        with pytest.raises(EntityError):
            Form(form_title='form_title', form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', creator_user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', vinculation_form_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', can_vinculate=True, template='template', area='area', system='system', street='street', city='city', number=99999, latitude=99999.99, longitude=99999.99, region='region', description='description', priority=PRIORITY.EMERGENCY, status=FORM_STATUS.IN_PROGRESS, expiration_date=946407600000, creation_date=946407600000, start_date=946407600000, conclusion_date=946407600000, justificative=justificative, comments='comments', sections=[section, section], information_fields=[])