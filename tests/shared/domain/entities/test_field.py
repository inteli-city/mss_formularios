import pytest
from src.shared.domain.entities.field import CheckBoxGroupField, CheckboxField, DateField, DropDownField, FileField, Field, NumberField, RadioGroupField, SwitchButtonField, TextField, TypeAheadField
from src.shared.domain.enums.fields_enum import FIELD_TYPE
from src.shared.domain.enums.file_type_enum import FILE_TYPE
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Field:

    def test_form_field_cannot_be_instanciated(self):
        with pytest.raises(TypeError):
            Field(field_type=FIELD_TYPE.TEXT_FIELD, placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting')

    def test_form_field_placeholder_is_none(self):
        with pytest.raises(EntityError):
            TextField(placeholder=None, required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='value')
    
    def test_form_field_placeholder_is_not_str(self):
        with pytest.raises(EntityError):
            TextField(placeholder=1, required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='value')
    
    def test_form_field_required_is_none(self):
        with pytest.raises(EntityError):
            TextField(placeholder='placeholder', required=None, key='key', regex='regex', formatting='formatting', max_length=10, value='value')
    
    def test_form_field_required_is_not_bool(self):
        with pytest.raises(EntityError):
            TextField(placeholder='placeholder', required='True', key='key', regex='regex', formatting='formatting', max_length=10, value='value')

    def test_form_field_key_is_none(self):
        with pytest.raises(EntityError):
            TextField(placeholder='placeholder', required=True, key=None, regex='regex', formatting='formatting', max_length=10, value='value')
    
    def test_form_field_key_is_not_str(self):
        with pytest.raises(EntityError):
            TextField(placeholder='placeholder', required=True, key=1, regex='regex', formatting='formatting', max_length=10, value='value')
    
    def test_form_field_regex_is_not_str(self):
        with pytest.raises(EntityError):
            TextField(placeholder='placeholder', required=True, key='key', regex=1, formatting='formatting', max_length=10, value='value')

    def test_form_field_formatting_is_not_str(self):
        with pytest.raises(EntityError):
            TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting=1, max_length=10, value='value')

    # TextField

    def test_text_field(self):
        text_field = TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=10, value='value')

        assert text_field.field_type == FIELD_TYPE.TEXT_FIELD
    
    def test_text_field_max_length_is_not_int(self):
        with pytest.raises(EntityError):
            TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length='10', value='value')
    
    def test_text_field_value_is_not_str(self):
        with pytest.raises(EntityError):
            TextField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_length=10, value=1)
    
    # NumberField

    def test_number_field(self):
        number_field = NumberField(placeholder='placeholder', required=True, key='key', regex ='regex', formatting='formatting', max_value=10, min_value=1, decimal=True, value=1.0)

        assert number_field.field_type == FIELD_TYPE.NUMBER_FIELD

    def test_number_field_max_value_is_not_int(self):
        with pytest.raises(EntityError):
            NumberField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_value='10', min_value=1, decimal=True, value=1)
    
    def test_number_field_min_value_is_not_int(self):
        with pytest.raises(EntityError):
            NumberField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_value=10, min_value='1', decimal=True, value=1)
    
    def test_number_field_decimal_is_none(self):
        with pytest.raises(EntityError):
            NumberField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_value=10, min_value=1, decimal=None, value=1)
    
    def test_number_field_decimal_is_not_bool(self):
        with pytest.raises(EntityError):
            NumberField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_value=10, min_value=1, decimal='True', value=1)
    
    def test_number_field_value_is_not_float(self):
        with pytest.raises(EntityError):
            NumberField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', max_value=10, min_value=1, decimal=True, value='1')
    

    # DropDownField

    def test_drop_down_field(self):
        dropdown_field = DropDownField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], value='option1')

        assert dropdown_field.field_type == FIELD_TYPE.DROPDOWN_FIELD

    def test_drop_down_field_options_is_not_list(self):
        with pytest.raises(EntityError):
            DropDownField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options='option1', value='option1')
    
    def test_drop_down_field_value_is_not_str(self):
        with pytest.raises(EntityError):
            DropDownField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], value=1)
    
    def test_drop_down_field_value_is_not_in_options(self):
        with pytest.raises(EntityError):
            DropDownField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], value='option3')
    
    # TypeAheadField

    def test_type_ahead_field(self):
        typeahead_field = TypeAheadField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], max_length=1, value='option1')

        assert typeahead_field.field_type == FIELD_TYPE.TYPEAHEAD_FIELD
    
    def test_type_ahead_field_options_is_not_list(self):
        with pytest.raises(EntityError):
            TypeAheadField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options='option1', max_length=1, value='option1')
    
    def test_type_ahead_field_max_length_is_not_int(self):
        with pytest.raises(EntityError):
            TypeAheadField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], max_length='1', value='option1')
    
    def test_type_ahead_field_value_is_not_str(self):
        with pytest.raises(EntityError):
            TypeAheadField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], max_length=1, value=1)
    
    # RadioGroupField

    def test_radio_group_field(self):
        radio_group_field = RadioGroupField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], value='option1')

        assert radio_group_field.field_type == FIELD_TYPE.RADIO_GROUP_FIELD
    
    def test_radio_group_field_options_is_not_list(self):
        with pytest.raises(EntityError):
            RadioGroupField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options='option1', value='option1')
    
    def test_radio_group_field_value_is_not_str(self):
        with pytest.raises(EntityError):
            RadioGroupField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], value=1)
    
    def test_radio_group_field_value_is_not_in_options(self):
        with pytest.raises(EntityError):
            RadioGroupField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], value='option3')
    
    # DateField

    def test_date_field(self):
        date_field = DateField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', min_date=946407600000, max_date=946407600000, value=946407600000)

        assert date_field.field_type == FIELD_TYPE.DATE_FIELD

    def test_date_field_min_date_is_not_int(self):
        with pytest.raises(EntityError):
            DateField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', min_date='946407600000', max_date=946407600000, value=946407600000)
    
    def test_date_field_min_date_is_not_timestamp(self):
        with pytest.raises(EntityError):
            DateField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', min_date=123, max_date=946407600000, value=946407600000)
    
    def test_date_field_max_date_is_not_int(self):
        with pytest.raises(EntityError):
            DateField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', min_date=946407600000, max_date='946407600000', value=946407600000)
    
    def test_date_field_max_date_is_not_timestamp(self):
        with pytest.raises(EntityError):
            DateField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', min_date=946407600000, max_date=123, value=946407600000)
    
    def test_date_field_value_is_not_int(self):
        with pytest.raises(EntityError):
            DateField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', min_date=946407600000, max_date=946407600000, value='946407600000')
    
    # CheckboxField

    def test_checkbox_field(self):
        checkbox_field = CheckboxField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', value=True)

        assert checkbox_field.field_type == FIELD_TYPE.CHECKBOX_FIELD
    
    def test_checkbox_field_value_is_not_bool(self):
        with pytest.raises(EntityError):
            CheckboxField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', value='True')

    # CheckboxGroupField

    def test_checkbox_group_field(self):
        checkbox_group_field = CheckBoxGroupField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], check_limit=1, value=['option1'])

        assert checkbox_group_field.field_type == FIELD_TYPE.CHECKBOX_GROUP_FIELD

    def test_checkbox_group_field_options_is_not_list(self):
        with pytest.raises(EntityError):
            CheckBoxGroupField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options='option1', check_limit=1, value=['option1'])
    
    def test_checkbox_group_field_check_limit_is_not_int(self):
        with pytest.raises(EntityError):
            CheckBoxGroupField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], check_limit='1', value=['option1'])
    
    def test_checkbox_group_field_check_limit_is_not_less_than_options_length(self):
        with pytest.raises(EntityError):
            CheckBoxGroupField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], check_limit=3, value=['option1'])
    
    def test_checkbox_group_field_value_is_not_list(self):
        with pytest.raises(EntityError):
            CheckBoxGroupField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], check_limit=1, value='option1')
    
    def test_checkbox_group_field_value_is_not_in_options(self):
        with pytest.raises(EntityError):
            CheckBoxGroupField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', options=['option1', 'option2'], check_limit=1, value=['option3', 'option1'])
    
    # SwitchButtonField

    def test_switch_button_field(self):
        switch_button_field = SwitchButtonField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', value=True)
    
        assert switch_button_field.field_type == FIELD_TYPE.SWITCH_BUTTON_FIELD
    
    def test_switch_button_field_value_is_not_bool(self):
        with pytest.raises(EntityError):
            SwitchButtonField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', value='True')
    
    # FileField

    def test_file_field(self):
        file_field = FileField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', file_type=FILE_TYPE.IMAGE, min_quantity=1, max_quantity=3, value=['file1', 'file2', 'file3'])

        assert file_field.field_type == FIELD_TYPE.FILE_FIELD
    
    def test_file_field_file_type_is_not_str(self):
        with pytest.raises(EntityError):
            FileField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', file_type=1, min_quantity=1, max_quantity=3, value=['file1'])
    
    def test_file_field_min_quantity_is_not_int(self):
        with pytest.raises(EntityError):
            FileField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', file_type=FILE_TYPE.IMAGE, min_quantity='1', max_quantity=3, value=['file1'])
    
    def test_file_field_max_quantity_is_not_int(self):
        with pytest.raises(EntityError):
            FileField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', file_type=FILE_TYPE.IMAGE, min_quantity=1, max_quantity='3', value=['file1'])
    
    def test_file_field_value_is_not_list(self):
        with pytest.raises(EntityError):
            FileField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', file_type=FILE_TYPE.IMAGE, min_quantity=1, max_quantity=3, value='file1')
    
    def test_file_field_value_is_not_str(self):
        with pytest.raises(EntityError):
            FileField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', file_type=FILE_TYPE.IMAGE, min_quantity=1, max_quantity=3, value=[1])
    
    def test_file_field_value_is_not_min_quantity(self):
        with pytest.raises(EntityError):
            FileField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', file_type=FILE_TYPE.IMAGE, min_quantity=2, max_quantity=3, value=['file1'])
    
    def test_file_field_value_is_not_max_quantity(self):
        with pytest.raises(EntityError):
            FileField(placeholder='placeholder', required=True, key='key', regex='regex', formatting='formatting', file_type=FILE_TYPE.IMAGE, min_quantity=1, max_quantity=2, value=['file1', 'file2', 'file3'])