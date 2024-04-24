import abc
from typing import Optional

from src.shared.domain.enums.fields_enum import FIELD_TYPE
from src.shared.helpers.errors.domain_errors import EntityError


class FormField(abc.ABC):
    field_type: FIELD_TYPE
    placeholder: str
    required: bool
    key: str
    regex: Optional[str]
    formatting: Optional[str]

    def __init__(self, field_type: FIELD_TYPE, placeholder: str, required: bool, key: str, regex: Optional[str], formatting: Optional[str]):
        if type(field_type) is not FIELD_TYPE:
            raise EntityError('field_type')
        self.field_type = field_type

        if type(placeholder) is not str:
            raise EntityError('placeholder')
        self.placeholder = placeholder

        if type(required) is not bool:
            raise EntityError('required')
        self.required = required

        if type(key) is not str:
            raise EntityError('key')
        self.key = key

        if regex is not None and type(regex) is not str:
            raise EntityError('regex')
        self.regex = regex

        if formatting is not None and type(formatting) is not str:
            raise EntityError('formatting')
        self.formatting = formatting

class TextField(FormField):
    max_length: Optional[int]
    value: Optional[str]

    def __init__(self, field_type: FIELD_TYPE, placeholder: str, required: bool, key: str, regex: Optional[str], formatting: Optional[str], max_length: int, value: str):
        super().__init__(field_type, placeholder, required, key, regex, formatting)
        if max_length is not None and type(max_length) is not int:
            raise EntityError('max_length')
        self.max_length = max_length

        if value is not None and type(value) is not str:
            raise EntityError('value')
        self.value = value

class NumberField(FormField):
    max_value: Optional[int]
    min_value: Optional[int]
    decimal: bool
    value: float

    def __init__(self, field_type: FIELD_TYPE, placeholder: str, required: bool, key: str, regex: Optional[str], formatting: Optional[str], max_value: int, min_value: int, decimal: bool, value: float):
        super().__init__(field_type, placeholder, required, key, regex, formatting)
        if max_value is not None and type(max_value) is not int:
            raise EntityError('max_value')
        self.max_value = max_value

        if min_value is not None and type(min_value) is not int:
            raise EntityError('min_value')
        self.min_value = min_value

        if type(decimal) is not bool:
            raise EntityError('decimal')
        self.decimal = decimal

        if value is not None and type(value) is not float:
            raise EntityError('value')
        self.value = value

