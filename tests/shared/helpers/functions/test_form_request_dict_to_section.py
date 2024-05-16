from src.shared.domain.entities.section import Section
from src.shared.helpers.functions.form_request_dict_to_section import dict_to_section


class Test_Function_dict_to_section:

    def test_dict_to_section(self):
        section = {
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
        
        result = dict_to_section(section)

        expected = Section(
            section_id='99999',
            fields=[
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
        )

        assert result == expected