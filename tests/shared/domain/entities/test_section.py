import pytest
from src.shared.domain.entities.field import TextField
from src.shared.domain.entities.section import Section
from src.shared.helpers.errors.domain_errors import EntityError

text_field = TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='value')
class Test_Section:

    def test_section(self):
        Section(section_id='99999', fields=[text_field, text_field])
    
    def test_section_id_not_str(self):
        with pytest.raises(EntityError):
            Section(section_id=99999, fields=[text_field])
    
    def test_section_fields_not_list(self):
        with pytest.raises(EntityError):
            Section(section_id='99999', fields=text_field)
    
    def test_section_fields_is_empty(self):
        with pytest.raises(EntityError):
            Section(section_id='99999', fields=[])
    
    def test_section_fields_not_field(self):
        with pytest.raises(EntityError):
            Section(section_id='99999', fields=['field'])
        