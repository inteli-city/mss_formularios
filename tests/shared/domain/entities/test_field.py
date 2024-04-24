from src.shared.domain.entities.field import FormField
from src.shared.domain.enums.fields_enum import FIELD_TYPE


class Test_Field:

    def test_field(self):
        FormField(field_type=FIELD_TYPE.TEXT, placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting')
    