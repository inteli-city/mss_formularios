from typing import List
from src.shared.domain.entities.field import Field
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.fields_enum import FIELD_TYPE
from src.shared.domain.enums.file_type_enum import FILE_TYPE
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.field import CheckBoxGroupField, CheckboxField, DateField, DropDownField, FileField, NumberField, RadioGroupField, SwitchButtonField, TextField, TypeAheadField

class SectionDTO:
    section_id: str
    fields: List[Field]

    def __init__(self, section_id: str, fields: List[Field]):
        self.section_id = section_id
        self.fields = fields
    
    @staticmethod
    def from_request(section_dict: dict) -> "SectionDTO":
        if section_dict.get('section_id') is None:
                raise MissingParameters('section_id')
        section_id = section_dict.get('section_id')

        if section_dict.get('fields') is None:
                raise MissingParameters('fields')
        if not section_dict.get('fields'):
            raise EntityError('fields')
        fields_data = section_dict.get('fields')

        fields = []

        for field_data in fields_data:

            if field_data.get('field_type') is None:
                raise MissingParameters('field_type')
            
            if field_data.get('field_type') not in [field.value for field in FIELD_TYPE]:
                raise EntityError('field_type')
            
            if field_data.get('placeholder') is None:
                raise MissingParameters('placeholder')
            
            if field_data.get('required') is None:
                raise MissingParameters('required')
            
            if field_data.get('key') is None:
                raise MissingParameters('key')
            
            field_type = FIELD_TYPE[field_data.get('field_type')]

            field_data.pop('field_type')

            if field_type == FIELD_TYPE.TEXT_FIELD:
                field = TextField(**field_data)

            elif field_type == FIELD_TYPE.NUMBER_FIELD:
                if field_data.get('decimal') is None:
                    raise MissingParameters('decimal')
                field = NumberField(**field_data)

            elif field_type == FIELD_TYPE.DROPDOWN_FIELD:
                if field_data.get('options') is None:
                    raise MissingParameters('options')
                field = DropDownField(**field_data)

            elif field_type == FIELD_TYPE.TYPEAHEAD_FIELD:
                if field_data.get('options') is None:
                    raise MissingParameters('options')
                field = TypeAheadField(**field_data)

            elif field_type == FIELD_TYPE.RADIO_GROUP_FIELD:
                if field_data.get('options') is None:
                    raise MissingParameters('options')
                field = RadioGroupField(**field_data)

            elif field_type == FIELD_TYPE.DATE_FIELD:
                field = DateField(**field_data)

            elif field_type == FIELD_TYPE.CHECKBOX_FIELD:
                field = CheckboxField(**field_data)

            elif field_type == FIELD_TYPE.CHECKBOX_GROUP_FIELD:
                if field_data.get('options') is None:
                    raise MissingParameters('options')
                field = CheckBoxGroupField(**field_data)

            elif field_type == FIELD_TYPE.SWITCH_BUTTON_FIELD:
                field = SwitchButtonField(**field_data)

            elif field_type == FIELD_TYPE.FILE_FIELD:
                if field_data.get('file_type') is None:
                    raise MissingParameters('file_type')
                if field_data.get('file_type') not in [file_type.value for file_type in FILE_TYPE]:
                    raise EntityError('file_type')
                if field_data.get('min_quantity') is None:
                    raise MissingParameters('min_quantity')
                if field_data.get('max_quantity') is None:
                    raise MissingParameters('max_quantity')
                field = FileField(
                    file_type=FILE_TYPE[field_data.get('file_type')],
                    min_quantity=field_data.get('min_quantity'),
                    max_quantity=field_data.get('max_quantity'),
                    formatting=field_data.get('formatting'),
                    key=field_data.get('key'),
                    placeholder=field_data.get('placeholder'),
                    regex=field_data.get('regex'),
                    required=field_data.get('required'),
                )

            else:
                raise EntityError('field_type')

            fields.append(field)

        return SectionDTO(section_id=section_id, fields=fields)

    def to_entity(self) -> Section:
        return Section(section_id=self.section_id, fields=self.fields)