from src.shared.domain.enums.information_field_type_enum import INFORMATION_FIELD_TYPE
from src.shared.helpers.errors.domain_errors import EntityError


class InformationFieldDTO():
    information_field_type: INFORMATION_FIELD_TYPE

    def __init__(self, information_field_type: INFORMATION_FIELD_TYPE):
        self.information_field_type = information_field_type
    
    def from_request(information_field_dict: dict) -> "InformationFieldDTO":
        if information_field_dict.get('information_field_type') is None and information_field_dict.get('information_field_type') not in [information_field.value for information_field in INFORMATION_FIELD_TYPE]:
                raise EntityError('information_field_type')
        information_field_type = INFORMATION_FIELD_TYPE[information_field_dict.get('information_field_type')]

        return InformationFieldDTO(information_field_type)