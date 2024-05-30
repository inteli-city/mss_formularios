from decimal import Decimal
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
    def from_dynamo(field_dict: dict):
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

        if field_type == FIELD_TYPE.TEXT_FIELD:
            field = TextField(
                placeholder=field_dict.get('placeholder'),
                required=field_dict.get('required'),
                key=field_dict.get('key'),
                regex=field_dict.get('regex'),
                formatting=field_dict.get('formatting'),
                max_length=int(field_dict.get('max_length')) if field_dict.get('max_length') is not None else None,
                value=field_dict.get('value'),
            )

        elif field_type == FIELD_TYPE.NUMBER_FIELD:
            if field_dict.get('decimal') is None:
                raise MissingParameters('decimal')
            field = NumberField(
                placeholder=field_dict.get('placeholder'),
                required=field_dict.get('required'),
                key=field_dict.get('key'),
                regex=field_dict.get('regex'),
                formatting=field_dict.get('formatting'),
                decimal=field_dict.get('decimal'),
                max_value=int(field_dict.get('max_value')) if field_dict.get('max_value') is not None else None,
                min_value=int(field_dict.get('min_value')) if field_dict.get('min_value') is not None else None,
                value=float(field_dict.get('value')) if field_dict.get('value') is not None else None,
            )

        elif field_type == FIELD_TYPE.DROPDOWN_FIELD:
            if field_dict.get('options') is None:
                raise MissingParameters('options')
            field = DropDownField(**field_dict)

        elif field_type == FIELD_TYPE.TYPEAHEAD_FIELD:
            if field_dict.get('options') is None:
                raise MissingParameters('options')
            field = TypeAheadField(
                placeholder=field_dict.get('placeholder'),
                required=field_dict.get('required'),
                key=field_dict.get('key'),
                regex=field_dict.get('regex'),
                formatting=field_dict.get('formatting'),
                options=field_dict.get('options'),
                max_length=int(field_dict.get('max_length')) if field_dict.get('max_length') is not None else None,
                value=field_dict.get('value')
            )

        elif field_type == FIELD_TYPE.RADIO_GROUP_FIELD:
            if field_dict.get('options') is None:
                raise MissingParameters('options')
            field = RadioGroupField(**field_dict)

        elif field_type == FIELD_TYPE.DATE_FIELD:
            field = DateField(
                placeholder=field_dict.get('placeholder'),
                required=field_dict.get('required'),
                key=field_dict.get('key'),
                regex=field_dict.get('regex'),
                formatting=field_dict.get('formatting'),
                min_date=int(field_dict.get('min_date')) if field_dict.get('min_date') is not None else None,
                max_date=int(field_dict.get('max_date')) if field_dict.get('max_date') is not None else None,
                value=int(field_dict.get('value')) if field_dict.get('value') is not None else None
            )

        elif field_type == FIELD_TYPE.CHECKBOX_FIELD:
            field = CheckboxField(**field_dict)

        elif field_type == FIELD_TYPE.CHECKBOX_GROUP_FIELD:
            if field_dict.get('options') is None:
                raise MissingParameters('options')
            field = CheckBoxGroupField(
                placeholder=field_dict.get('placeholder'),
                required=field_dict.get('required'),
                key=field_dict.get('key'),
                regex=field_dict.get('regex'),
                formatting=field_dict.get('formatting'),
                options=field_dict.get('options'),
                check_limit=int(field_dict.get('check_limit')) if field_dict.get('check_limit') is not None else None,
                value=field_dict.get('value')
            )

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
                formatting=field_dict.get('formatting'),
                key=field_dict.get('key'),
                placeholder=field_dict.get('placeholder'),
                regex=field_dict.get('regex'),
                required=field_dict.get('required'),
                file_type=FILE_TYPE[field_dict.get('file_type')],
                min_quantity=int(field_dict.get('min_quantity')) if field_dict.get('min_quantity') is not None else None,
                max_quantity=int(field_dict.get('max_quantity')) if field_dict.get('max_quantity') is not None else None,
                value=field_dict.get('value')
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
                "max_value": Decimal(str(self.field.max_value)) if self.field.max_value is not None else None,
                "min_value": Decimal(str(self.field.min_value)) if self.field.min_value is not None else None,
                "decimal": self.field.decimal,
                "value": Decimal(str(self.field.value)) if self.field.value is not None else None
            })
        elif isinstance(self.field, DropDownField):
            dynamo_dict.update({
                "options": self.field.options,
                "value": self.field.value
            })
        elif isinstance(self.field, TypeAheadField):
            dynamo_dict.update({
                "options": self.field.options,
                "max_length": Decimal(str(self.field.max_length)) if self.field.max_length is not None else None,
                "value": self.field.value
            })
        elif isinstance(self.field, RadioGroupField):
            dynamo_dict.update({
                "options": self.field.options,
                "value": self.field.value
            })
        elif isinstance(self.field, DateField):
            dynamo_dict.update({
                "min_date": Decimal(str(self.field.min_date)) if self.field.min_date is not None else None,
                "max_date": Decimal(str(self.field.max_date)) if self.field.max_date is not None else None,
                "value": self.field.value
            })
        elif isinstance(self.field, CheckboxField):
            dynamo_dict.update({
                "value": self.field.value
            })
        elif isinstance(self.field, CheckBoxGroupField):
            dynamo_dict.update({
                "options": self.field.options,
                "check_limit": Decimal(str(self.field.check_limit)) if self.field.check_limit is not None else None,
                "value": self.field.value
            })
        elif isinstance(self.field, SwitchButtonField):
            dynamo_dict.update({
                "value": self.field.value
            })
        elif isinstance(self.field, FileField):
            dynamo_dict.update({
                "file_type": self.field.file_type.name,
                "min_quantity": Decimal(str(self.field.min_quantity)),
                "max_quantity": Decimal(str(self.field.max_quantity)),
                "value": self.field.value
            })

        return dynamo_dict

    def to_entity(self) -> Field:
        return self.field
