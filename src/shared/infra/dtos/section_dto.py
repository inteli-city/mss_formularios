from typing import List
from src.shared.domain.entities.field import Field
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.fields_enum import FIELD_TYPE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.entities.field import CheckBoxGroupField, CheckboxField, DateField, DropDownField, FileField, NumberField, RadioGroupField, SwitchButtonField, TextField, TypeAheadField

class SectionDTO:
    section_id: str
    fields: List[Field]

    def __init__(self, section_id: str, fields: List[Field]):
        self.section_id = section_id
        self.fields = fields
    
    def from_request(section_dict: dict) -> "SectionDTO":
        if section_dict.get('section_id') is None:
                raise EntityError('section_id')
        section_id = section_dict.get('section_id')

        if section_dict.get('fields') is None or not section_dict.get('fields'):
                raise EntityError('fields')
        fields_data = section_dict.get('fields')

        fields = []

        for field_data in fields_data:

            if field_data.get('field_type') is None:
                raise EntityError('field_type')
            
            if field_data.get('field_type') not in [field.value for field in FIELD_TYPE]:
                raise EntityError('field_type')
            
            field_type = FIELD_TYPE[field_data.get('field_type')]

            field_data.pop('field_type')

            if field_type == FIELD_TYPE.TEXT_FIELD:
                field = TextField(**field_data)
            elif field_type == FIELD_TYPE.NUMBER_FIELD:
                field = NumberField(**field_data)
            elif field_type == FIELD_TYPE.DROP_DOWN_FIELD:
                field = DropDownField(**field_data)
            elif field_type == FIELD_TYPE.TYPE_AHEAD_FIELD:
                field = TypeAheadField(**field_data)
            elif field_type == FIELD_TYPE.RADIO_GROUP_FIELD:
                field = RadioGroupField(**field_data)
            elif field_type == FIELD_TYPE.DATE_FIELD:
                field = DateField(**field_data)
            elif field_type == FIELD_TYPE.CHECKBOX_FIELD:
                field = CheckboxField(**field_data)
            elif field_type == FIELD_TYPE.CHECKBOX_GROUP_FIELD:
                field = CheckBoxGroupField(**field_data)
            elif field_type == FIELD_TYPE.SWITCH_BUTTON_FIELD:
                field = SwitchButtonField(**field_data)
            elif field_type == FIELD_TYPE.FILE_FIELD:
                field = FileField(**field_data)
            else:
                raise EntityError('field_type')

            fields.append(field)

        return SectionDTO(section_id=section_id, fields=fields)

    def to_entity(self) -> Section:
        return Section(section_id=self.section_id, fields=self.fields)