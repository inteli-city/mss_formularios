from typing import Dict, Any, Union

from src.shared.domain.entities.field import CheckBoxGroupField, CheckboxField, DateField, DropDownField, Field, FileField, NumberField, RadioGroupField, SwitchButtonField, TextField, TypeAheadField
from src.shared.domain.enums.fields_enum import FIELD_TYPE
from src.shared.domain.enums.file_type_enum import FILE_TYPE
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError

class FieldDTO:
    field: Field

    def __init__(self, field: Field):
        self.field = field
    
    @staticmethod
    def from_dict(field_dict: dict):
        if field_dict.get('field_type') is None:
            raise MissingParameters('field_type')
        
        if field_dict.get('field_type') not in [field.value for field in FIELD_TYPE]:
            raise EntityError('field_type')
        
        if field_dict.get('placeholder') is None:
            raise MissingParameters('placeholder')
        
        if field_dict.get('required') is None:
            raise MissingParameters('required')
        
        if field_dict.get('key') is None:
            raise MissingParameters('key')
        
        field_type = FIELD_TYPE[field_dict.get('field_type')]

        field_dict.pop('field_type')

        print(field_dict)

        if field_type == FIELD_TYPE.TEXT_FIELD:
            field = TextField(**field_dict)

        elif field_type == FIELD_TYPE.NUMBER_FIELD:
            if field_dict.get('decimal') is None:
                raise MissingParameters('decimal')
            field = NumberField(**field_dict)

        elif field_type == FIELD_TYPE.DROPDOWN_FIELD:
            if field_dict.get('options') is None:
                raise MissingParameters('options')
            field = DropDownField(**field_dict)

        elif field_type == FIELD_TYPE.TYPEAHEAD_FIELD:
            if field_dict.get('options') is None:
                raise MissingParameters('options')
            field = TypeAheadField(**field_dict)

        elif field_type == FIELD_TYPE.RADIO_GROUP_FIELD:
            if field_dict.get('options') is None:
                raise MissingParameters('options')
            field = RadioGroupField(**field_dict)

        elif field_type == FIELD_TYPE.DATE_FIELD:
            field = DateField(**field_dict)

        elif field_type == FIELD_TYPE.CHECKBOX_FIELD:
            field = CheckboxField(**field_dict)

        elif field_type == FIELD_TYPE.CHECKBOX_GROUP_FIELD:
            if field_dict.get('options') is None:
                raise MissingParameters('options')
            field = CheckBoxGroupField(**field_dict)

        elif field_type == FIELD_TYPE.SWITCH_BUTTON_FIELD:
            field = SwitchButtonField(**field_dict)

        elif field_type == FIELD_TYPE.FILE_FIELD:
            if field_dict.get('file_type') is None:
                raise MissingParameters('file_type')
            if field_dict.get('file_type') not in [file_type.value for file_type in FILE_TYPE]:
                raise EntityError('file_type')
            if field_dict.get('min_quantity') is None:
                raise MissingParameters('min_quantity')
            if field_dict.get('max_quantity') is None:
                raise MissingParameters('max_quantity')
            field = FileField(
                file_type=FILE_TYPE[field_dict.get('file_type')],
                min_quantity=field_dict.get('min_quantity'),
                max_quantity=field_dict.get('max_quantity'),
                formatting=field_dict.get('formatting'),
                key=field_dict.get('key'),
                placeholder=field_dict.get('placeholder'),
                regex=field_dict.get('regex'),
                required=field_dict.get('required'),
            )
        
        return FieldDTO(field)

    def to_dynamo(self) -> dict:
        dynamo_dict = {
            "field_type": self.field.field_type.name,
            "placeholder": self.field.placeholder,
            "required": self.field.required,
            "key": self.field.key,
            "regex": self.field.regex,
            "formatting": self.field.formatting
        }

        if isinstance(self.field, TextField):
            dynamo_dict.update({
                "max_length": self.field.max_length,
                "value": self.field.value
            })
        elif isinstance(self.field, NumberField):
            dynamo_dict.update({
                "max_value": self.field.max_value,
                "min_value": self.field.min_value,
                "decimal": self.field.decimal,
                "value": self.field.value
            })
        elif isinstance(self.field, DropDownField):
            dynamo_dict.update({
                "options": self.field.options,
                "value": self.field.value
            })
        elif isinstance(self.field, TypeAheadField):
            dynamo_dict.update({
                "options": self.field.options,
                "max_length": self.field.max_length,
                "value": self.field.value
            })
        elif isinstance(self.field, RadioGroupField):
            dynamo_dict.update({
                "options": self.field.options,
                "value": self.field.value
            })
        elif isinstance(self.field, DateField):
            dynamo_dict.update({
                "min_date": self.field.min_date,
                "max_date": self.field.max_date,
                "value": self.field.value
            })
        elif isinstance(self.field, CheckboxField):
            dynamo_dict.update({
                "value": self.field.value
            })
        elif isinstance(self.field, CheckBoxGroupField):
            dynamo_dict.update({
                "options": self.field.options,
                "check_limit": self.field.check_limit,
                "value": self.field.value
            })
        elif isinstance(self.field, SwitchButtonField):
            dynamo_dict.update({
                "value": self.field.value
            })
        elif isinstance(self.field, FileField):
            dynamo_dict.update({
                "file_type": self.field.file_type.name,
                "min_quantity": self.field.min_quantity,
                "max_quantity": self.field.max_quantity,
                "value": self.field.value
            })

        return dynamo_dict

    def to_entity(self) -> Field:
        return self.field
