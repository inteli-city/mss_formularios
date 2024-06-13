import abc
import re
from typing import List, Optional

from src.shared.domain.enums.fields_enum import FIELD_TYPE
from src.shared.domain.enums.file_type_enum import FILE_TYPE
from src.shared.helpers.errors.domain_errors import EntityError


class Field(abc.ABC):
    field_type: FIELD_TYPE
    placeholder: str
    required: bool
    key: str
    regex: Optional[str]
    formatting: Optional[str]


    @abc.abstractmethod
    def __init__(self, field_type: FIELD_TYPE, placeholder: str, required: bool, key: str, regex: Optional[str] = None, formatting: Optional[str] = None):
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

class TextField(Field):
    max_length: Optional[int]
    value: Optional[str]

    def __init__(self, placeholder: str, required: bool, key: str, max_length: int, formatting: Optional[str] = None, regex: Optional[str] = None, value: Optional[str] = None):
        super().__init__(FIELD_TYPE.TEXT_FIELD, placeholder, required, key, regex, formatting)
        if max_length is not None and type(max_length) is not int:
            raise EntityError('max_length')
        self.max_length = max_length

        if value is not None:
            if type(value) is not str:
                raise EntityError('value')
            if max_length is not None and len(value) > max_length:
                raise EntityError('value')
        self.value = value

class NumberField(Field):
    max_value: Optional[int]
    min_value: Optional[int]
    decimal: bool
    value: Optional[float]

    def __init__(self, placeholder: str, required: bool, key: str, decimal: bool, max_value: int = None, min_value: int = None, regex: Optional[str] = None, formatting: Optional[str] = None, value: Optional[float] = None):
        super().__init__(FIELD_TYPE.NUMBER_FIELD, placeholder, required, key, regex, formatting)
        if max_value is not None and type(max_value) is not int:
            raise EntityError('max_value')
        self.max_value = max_value

        if min_value is not None and type(min_value) is not int:
            raise EntityError('min_value')
        self.min_value = min_value

        if type(decimal) is not bool:
            raise EntityError('decimal')
        self.decimal = decimal

        if value is not None:
            if type(value) is not float:
                raise EntityError('value')
            if min_value is not None and value < min_value:
                raise EntityError('value')
            if max_value is not None and value > max_value:
                raise EntityError('value')
        self.value = value

class DropDownField(Field):
    options: List[str]
    value: Optional[str]

    def __init__(self, placeholder: str, required: bool, key: str, options: List[str], regex: Optional[str] = None, formatting: Optional[str] = None, value: Optional[str] = None):
        super().__init__(FIELD_TYPE.DROPDOWN_FIELD, placeholder, required, key, regex, formatting)
        if type(options) is not list:
            raise EntityError('options')
        self.options = options

        if value is not None and (type(value) is not str or value not in options):
            raise EntityError('value')
        self.value = value

class TypeAheadField(Field):
    options: List[str]
    max_length: Optional[int]
    value: Optional[str]

    def __init__(self, placeholder: str, required: bool, key: str, options: List[str], max_length: Optional[int] = None, regex: Optional[str] = None, formatting: Optional[str] = None, value: Optional[str] = None):
        super().__init__(FIELD_TYPE.TYPEAHEAD_FIELD, placeholder, required, key, regex, formatting)
        if type(options) is not list:
            raise EntityError('options')
        self.options = options

        if max_length is not None and type(max_length) is not int:
            raise EntityError('max_length')
        self.max_length = max_length

        if value is not None and type(value) is not str:
            raise EntityError('value')
        self.value = value

class RadioGroupField(Field):
    options: List[str]
    value: Optional[str]

    def __init__(self, placeholder: str, required: bool, key: str, options: List[str], regex: Optional[str] = None, formatting: Optional[str] = None, value: Optional[str] = None):
        super().__init__(FIELD_TYPE.RADIO_GROUP_FIELD, placeholder, required, key, regex, formatting)
        if type(options) is not list:
            raise EntityError('options')
        self.options = options

        if value is not None and (type(value) is not str or value not in options):
            raise EntityError('value')
        self.value = value

class DateField(Field):
    min_date: Optional[int] # timestamp
    max_date: Optional[int] # timestamp
    value: Optional[int] # timestamp

    def __init__(self, placeholder: str, required: bool, key: str, min_date: Optional[int] = None, max_date: Optional[int] = None, regex: Optional[str] = None, formatting: Optional[str] = None, value: Optional[int] = None):
        super().__init__(FIELD_TYPE.DATE_FIELD, placeholder, required, key, regex, formatting)
        if min_date is not None and type(min_date) is not int:
            raise EntityError('min_date')
        self.min_date = min_date

        if max_date is not None and type(max_date) is not int:
            raise EntityError('max_date')
        self.max_date = max_date

        if value is not None: 
            if type(value) is not int:
                raise EntityError('value')
            if min_date is not None and value < min_date:
                raise EntityError('value')
            if max_date is not None and value > max_date:
                raise EntityError('value')
        self.value = value
    

class CheckboxField(Field):
    value: Optional[bool]

    def __init__(self, placeholder: str, required: bool, key: str, regex: Optional[str] = None, formatting: Optional[str] = None, value: Optional[bool] = None):
        super().__init__(FIELD_TYPE.CHECKBOX_FIELD, placeholder, required, key, regex, formatting)
        if value is not None and type(value) is not bool:
            raise EntityError('value')
        self.value = value

class CheckBoxGroupField(Field):
    options: List[str]
    check_limit: Optional[int]
    value: Optional[List[str]]

    def __init__(self, placeholder: str, required: bool, key: str, options: List[str], check_limit: Optional[int] = None, regex: Optional[str] = None, formatting: Optional[str] = None, value: Optional[List[str]] = None):
        super().__init__(FIELD_TYPE.CHECKBOX_GROUP_FIELD, placeholder, required, key, regex, formatting)
        if type(options) is not list:
            raise EntityError('options')
        self.options = options

        if check_limit is not None:
            if type(check_limit) is not int:
                raise EntityError('check_limit')
            if check_limit > len(options):
                raise EntityError('check_limit')
        self.check_limit = check_limit

        if value is not None: 
            if type(value) is not list or not all([type(val) is str for val in value]) or not all([val in options for val in value]):
                raise EntityError('value')
            if check_limit is not None and len(value) > check_limit:
                raise EntityError('value')
        self.value = value

class SwitchButtonField(Field):
    value: Optional[bool]

    def __init__(self, placeholder: str, required: bool, key: str, regex: Optional[str] = None, formatting: Optional[str] = None, value: Optional[bool] = None,):
        super().__init__(FIELD_TYPE.SWITCH_BUTTON_FIELD, placeholder, required, key, regex, formatting)
        if value is not None and type(value) is not bool:
            raise EntityError('value')
        self.value = value

class FileField(Field):
    file_type: FILE_TYPE
    min_quantity: int
    max_quantity: int
    value: Optional[List[str]]

    def __init__(self, placeholder: str, required: bool, key: str, file_type: FILE_TYPE, min_quantity: int, max_quantity: int, regex: Optional[str] = None, formatting: Optional[str] = None, value: Optional[List[str]] = None):
        super().__init__(FIELD_TYPE.FILE_FIELD, placeholder, required, key, regex, formatting)
        if type(file_type) is not FILE_TYPE:
            raise EntityError('file_type')
        self.file_type = file_type

        if type(min_quantity) is not int:
            raise EntityError('min_quantity')
        self.min_quantity = min_quantity

        if type(max_quantity) is not int:
            raise EntityError('max_quantity')
        self.max_quantity = max_quantity

        if value is not None:
            if not isinstance(value, list):
                raise EntityError('value')
            if not all(isinstance(item, str) for item in value):
                raise EntityError('value')
            if not min_quantity <= len(value) <= max_quantity:
                raise EntityError('value')
        self.value = value