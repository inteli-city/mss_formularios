from src.shared.domain.entities.field import TextField
from src.shared.domain.enums.fields_enum import FIELD_TYPE
from src.shared.infra.dtos.section_dto import SectionDTO


class Test_SectionDTO:

    def test_section_dto_from_request(self):
        section_dict = {
            'section_id': '99999',
            'fields': [
                {
                    'field_type': 'TEXT_FIELD',
                    'placeholder': 'placeholder',
                    'required': True,
                    'key': 'key',
                    'regex': 'regex',
                    'formatting': 'formatting',
                    'max_length': 10,
                    'value': 'value'
                },
                {
                    'field_type': 'TEXT_FIELD',
                    'placeholder': 'placeholder',
                    'required': True,
                    'key': 'key',
                    'regex': 'regex',
                    'formatting': 'formatting',
                    'max_length': 10,
                    'value': 'value'
                }
            ]
        }

        section = SectionDTO.from_request(section_dict)

        assert section.section_id == '99999'
        assert len(section.fields) == 2
        assert section.fields[0].field_type == FIELD_TYPE.TEXT_FIELD
        assert section.fields[0].placeholder == 'placeholder'
        assert section.fields[0].required == True
        assert section.fields[0].key == 'key'
        assert section.fields[0].regex == 'regex'
        assert section.fields[0].formatting == 'formatting'
        assert section.fields[0].max_length == 10
        assert section.fields[0].value == 'value'

        assert section.fields[1].field_type == FIELD_TYPE.TEXT_FIELD
        assert section.fields[1].placeholder == 'placeholder'
        assert section.fields[1].required == True
        assert section.fields[1].key == 'key'
        assert section.fields[1].regex == 'regex'
        assert section.fields[1].formatting == 'formatting'
        assert section.fields[1].max_length == 10
        assert section.fields[1].value == 'value'
    
    def test_section_dto_to_entity(self):
        section_dto = SectionDTO(
            section_id='99999',
            fields=[
                TextField(
                    placeholder='placeholder',
                    required=True,
                    key='key',
                    regex='regex',
                    formatting='formatting',
                    max_length=10,
                    value='value'
                ),
            ]
        )

        section = section_dto.to_entity()

        assert section.section_id == '99999'
        assert len(section.fields) == 1
        assert section.fields[0].field_type == FIELD_TYPE.TEXT_FIELD
        assert section.fields[0].placeholder == 'placeholder'
        assert section.fields[0].required == True
        assert section.fields[0].key == 'key'
        assert section.fields[0].regex == 'regex'
        assert section.fields[0].formatting == 'formatting'
        assert section.fields[0].max_length == 10
        assert section.fields[0].value == 'value'
        