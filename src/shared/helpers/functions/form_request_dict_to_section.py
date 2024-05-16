from src.shared.domain.entities.field import CheckBoxGroupField, CheckboxField, DateField, DropDownField, FileField, NumberField, RadioGroupField, SwitchButtonField, TextField, TypeAheadField
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.fields_enum import FIELD_TYPE
from src.shared.helpers.errors.domain_errors import EntityError


def dict_to_section(json_data: dict) -> Section:
    section_id = json_data.get('section_id')
    fields_data = json_data.get('fields', [])
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
        print(type(field))

        fields.append(field)


    return Section(section_id=section_id, fields=fields)