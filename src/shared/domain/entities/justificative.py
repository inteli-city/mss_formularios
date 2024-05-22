import abc
from typing import List, Optional

from src.shared.helpers.errors.domain_errors import EntityError


class JustificativeOption(abc.ABC):
    option: str
    required_image: bool
    required_text: bool

    def __init__(self, option: str, required_image: bool, required_text: bool):
        if type(option) is not str:
            raise EntityError('option')
        self.option = option

        if type(required_image) is not bool:
            raise EntityError('required_image')
        self.required_image = required_image

        if type(required_text) is not bool:
            raise EntityError('required_text')
        self.required_text = required_text

class Justificative(abc.ABC):
    options: List[JustificativeOption]
    selected_option: Optional[str]
    text: Optional[str]
    image: Optional[str]

    def __init__(self, options: List[JustificativeOption], selected_option: Optional[str], text: Optional[str], image: Optional[str]):
        if type(options) is not list:
            raise EntityError('options')
        for option in options:
            if type(option) is not JustificativeOption:
                raise EntityError('options')
        self.options = options

        if selected_option is not None and type(selected_option) is not str:
            raise EntityError('selected_option')
        self.selected_option = selected_option

        if text is not None and type(text) is not str:
            raise EntityError('text')
        self.text = text

        if image is not None and type(image) is not str:
            raise EntityError('image')
        self.image = image