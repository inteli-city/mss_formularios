import abc
from typing import List, Optional

from src.shared.helpers.errors.domain_errors import EntityError


class JustificationOption(abc.ABC):
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

class Justification(abc.ABC):
    options: List[JustificationOption]
    selected_option: Optional[str]
    justification_text: Optional[str]
    justification_image: Optional[str]

    def __init__(self, options: List[JustificationOption], selected_option: Optional[str], justification_text: Optional[str], justification_image: Optional[str]):
        if type(options) is not list:
            raise EntityError('options')
        for option in options:
            if type(option) is not JustificationOption:
                raise EntityError('options')
        self.options = options

        if selected_option is not None and type(selected_option) is not str:
            raise EntityError('selected_option')
        self.selected_option = selected_option

        if justification_text is not None and type(justification_text) is not str:
            raise EntityError('justification_text')
        self.justification_text = justification_text

        if justification_image is not None and type(justification_image) is not str:
            raise EntityError('justification_image')
        self.justification_image = justification_image