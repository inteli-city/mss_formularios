from typing import List, Optional
from src.shared.domain.entities.justification import Justification, JustificationOption
from src.shared.helpers.errors.domain_errors import EntityError


class JustificationDTO:
    options: List[JustificationOption]
    selected_option: Optional[str]
    justification_text: Optional[str]
    justification_image: Optional[str]

    def __init__(self, options: List[JustificationOption], selected_option: Optional[str], justification_text: Optional[str], justification_image: Optional[str]):
        self.options = options
        self.selected_option = selected_option
        self.justification_text = justification_text
        self.justification_image = justification_image

    def from_request(justification_dict: dict) -> "JustificationDTO":
        if justification_dict.get('options') is None or not justification_dict.get('options'):
            raise EntityError('options')
        options_data = justification_dict.get('options')

        options = []

        for option_data in options_data:
            if option_data.get('option') is None:
                raise EntityError('option')

            if option_data.get('required_image') is None:
                raise EntityError('required_image')

            if option_data.get('required_text') is None:
                raise EntityError('required_text')

            option = JustificationOption(**option_data)
            options.append(option)

        selected_option = justification_dict.get('selected_option')
        justification_text = justification_dict.get('justification_text')
        justification_image = justification_dict.get('justification_image')

        return JustificationDTO(options=options, selected_option=selected_option, justification_text=justification_text, justification_image=justification_image)

    @staticmethod
    def from_entity(justification: Justification) -> "JustificationDTO":
        return JustificationDTO(options=justification.options, selected_option=justification.selected_option, justification_text=justification.justification_text, justification_image=justification.justification_image)
    
    def to_dynamo(self) -> dict:
        return {
            "options": [{
                "option": option.option,
                "required_image": option.required_image,
                "required_text": option.required_text
            } for option in self.options],
            "selected_option": self.selected_option,
            "justification_text": self.justification_text,
            "justification_image": self.justification_image
        }

    @staticmethod
    def from_dynamo(justification_dict: dict) -> "JustificationDTO":
        options_data = justification_dict.get('options')

        options = [JustificationOption(**option_data) for option_data in options_data]

        selected_option = justification_dict.get('selected_option')
        justification_text = justification_dict.get('justification_text')
        justification_image = justification_dict.get('justification_image')

        return JustificationDTO(options=options, selected_option=selected_option, justification_text=justification_text, justification_image=justification_image)

    def to_entity(self) -> Justification:
        return Justification(options=self.options, selected_option=self.selected_option, justification_text=self.justification_text, justification_image=self.justification_image)