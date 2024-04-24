import abc

from src.shared.domain.enums.information_field_type_enum import INFORMATION_FIELD_TYPE
from src.shared.helpers.errors.domain_errors import EntityError


class InformationField(abc.ABC):
    information_field_type: INFORMATION_FIELD_TYPE

    @abc.abstractmethod
    def __init__(self, information_field_type: INFORMATION_FIELD_TYPE):
        if type(information_field_type) is not INFORMATION_FIELD_TYPE:
            raise EntityError('information_field_type')
        self.information_field_type = information_field_type

class TextInformationField(InformationField):
    value: str

    def __init__(self, value: str):
        super().__init__(information_field_type=INFORMATION_FIELD_TYPE.TEXT_INFORMATION_FIELD)
        if type(value) is not str:
            raise EntityError('value')
        self.value = value

class MapInformationField(InformationField):
    latitude: float
    longitude: float

    def __init__(self, latitude: float, longitude: float):
        super().__init__(information_field_type=INFORMATION_FIELD_TYPE.MAP_INFORMATION_FIELD)
        if type(latitude) is not float:
            raise EntityError('latitude')
        self.latitude = latitude

        if type(longitude) is not float:
            raise EntityError('longitude')
        self.longitude = longitude

class ImageInformationField(InformationField):
    file_path: str

    def __init__(self, file_path: str):
        super().__init__(information_field_type=INFORMATION_FIELD_TYPE.IMAGE_INFORMATION_FIELD)
        if type(file_path) is not str:
            raise EntityError('file_path')
        self.file_path = file_path