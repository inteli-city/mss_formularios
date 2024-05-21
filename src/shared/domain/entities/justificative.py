import abc
from typing import List, Optional

from src.shared.helpers.errors.domain_errors import EntityError


class JustificativeOption(abc.ABC):
    option: str
    requiredImage: bool
    requiredText: bool

    def __init__(self, option: str, requiredImage: bool, requiredText: bool):
        if type(option) is not str:
            raise EntityError('option')
        self.option = option

        if type(requiredImage) is not bool:
            raise EntityError('requiredImage')
        self.requiredImage = requiredImage

        if type(requiredText) is not bool:
            raise EntityError('requiredText')
        self.requiredText = requiredText

class Justificative(abc.ABC):
    options: List[JustificativeOption]
    selectedOption: Optional[str]
    text: Optional[str]
    image: Optional[str]

    def __init__(self, options: List[JustificativeOption], selectedOption: Optional[str], text: Optional[str], image: Optional[str]):
        if type(options) is not list:
            raise EntityError('options')
        for option in options:
            if type(option) is not JustificativeOption:
                raise EntityError('options')
        self.options = options

        if selectedOption is not None and type(selectedOption) is not str:
            raise EntityError('selectedOption')
        self.selectedOption = selectedOption

        if text is not None and type(text) is not str:
            raise EntityError('text')
        self.text = text

        if image is not None and type(image) is not str:
            raise EntityError('image')
        self.image = image