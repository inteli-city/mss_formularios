import pytest
from src.shared.domain.enums.information_field_type_enum import INFORMATION_FIELD_TYPE
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.infra.dtos.information_field_dto import InformationFieldDTO


class Test_InformationFieldDTO:

    def test_information_field_from_request_text(self):
        information_field_dict = {
            'information_field_type': 'TEXT_INFORMATION_FIELD',
            'value': 'value'
        }
        information_field_dto = InformationFieldDTO.from_request(information_field_dict)
        assert information_field_dto.information_field.value == 'value'
        assert information_field_dto.information_field.information_field_type == INFORMATION_FIELD_TYPE.TEXT_INFORMATION_FIELD
    
    def test_information_field_from_request_map(self):
        information_field_dict = {
            'information_field_type': 'MAP_INFORMATION_FIELD',
            'latitude': 0.0,
            'longitude': 0.0
        }
        information_field_dto = InformationFieldDTO.from_request(information_field_dict)
        assert information_field_dto.information_field.latitude == 0.0
        assert information_field_dto.information_field.longitude == 0.0
        assert information_field_dto.information_field.information_field_type == INFORMATION_FIELD_TYPE.MAP_INFORMATION_FIELD
    
    def test_information_field_from_request_image(self):
        information_field_dict = {
            'information_field_type': 'IMAGE_INFORMATION_FIELD',
            'file_path': 'file_path'
        }
        information_field_dto = InformationFieldDTO.from_request(information_field_dict)
        assert information_field_dto.information_field.file_path == 'file_path'
        assert information_field_dto.information_field.information_field_type == INFORMATION_FIELD_TYPE.IMAGE_INFORMATION_FIELD
    
    def test_information_field_from_request_missing_information_field_type(self):
        information_field_dict = {
            'value': 'value'
        }

        with pytest.raises(MissingParameters):
            InformationFieldDTO.from_request(information_field_dict)
    
    def test_information_field_from_request_text_information_field_missing_value(self):
        information_field_dict = {
            'information_field_type': 'TEXT_INFORMATION_FIELD'
        }

        with pytest.raises(MissingParameters):
            InformationFieldDTO.from_request(information_field_dict)
    
    def test_information_field_from_request_map_information_field_missing_latitude(self):
        information_field_dict = {
            'information_field_type': 'MAP_INFORMATION_FIELD',
            'longitude': 0.0
        }

        with pytest.raises(MissingParameters):
            InformationFieldDTO.from_request(information_field_dict)
    
    def test_information_field_from_request_map_information_field_missing_longitude(self):
        information_field_dict = {
            'information_field_type': 'MAP_INFORMATION_FIELD',
            'latitude': 0.0
        }

        with pytest.raises(MissingParameters):
            InformationFieldDTO.from_request(information_field_dict)
    
    def test_information_field_from_request_image_information_field_missing_file_path(self):
        information_field_dict = {
            'information_field_type': 'IMAGE_INFORMATION_FIELD'
        }

        with pytest.raises(MissingParameters):
            InformationFieldDTO.from_request(information_field_dict)
    
    def test_information_field_to_entity(self):
        information_field_dict = {
            'information_field_type': 'TEXT_INFORMATION_FIELD',
            'value': 'value'
        }
        information_field_dto = InformationFieldDTO.from_request(information_field_dict)
        information_field = information_field_dto.to_entity()
        assert information_field.value == 'value'
        assert information_field.information_field_type == INFORMATION_FIELD_TYPE.TEXT_INFORMATION_FIELD