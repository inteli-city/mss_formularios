from src.shared.domain.entities.justificative import Justificative, JustificativeOption
from src.shared.helpers.errors.domain_errors import EntityError


class JustificativeDTO:
    justificative: Justificative

    def __init__(self, justificative: Justificative):
        self.justificative = justificative

    def from_request(justificative_dict: dict) -> "JustificativeDTO":
        if justificative_dict.get('options') is None or not justificative_dict.get('options'):
            raise EntityError('options')
        options_data = justificative_dict.get('options')

        options = []

        for option_data in options_data:
            if option_data.get('option') is None:
                raise EntityError('option')

            if option_data.get('required_image') is None:
                raise EntityError('required_image')

            if option_data.get('required_text') is None:
                raise EntityError('required_text')

            option = JustificativeOption(**option_data)
            options.append(option)

        selected_option = justificative_dict.get('selected_option')
        text = justificative_dict.get('text')
        image = justificative_dict.get('image')

        return JustificativeDTO(Justificative(options=options, selected_option=selected_option, text=text, image=image))

    def to_entity(self) -> Justificative:
        return self.justificative