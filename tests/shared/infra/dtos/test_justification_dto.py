import pytest
from src.shared.domain.entities.justification import Justification, JustificationOption
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.dtos.justification_dto import JustificationDTO


class Test_justificationDTO:

    def test_justification_dto_from_request(self):
        justification_dict = {
            'options': [
                {
                    'option': 'option',
                    'required_image': True,
                    'required_text': True
                }
            ],
            'selected_option': 'selected_option',
            'justification_text': 'text',
            'justification_image': 'image'
        }

        justification = JustificationDTO.from_request(justification_dict)

        assert len(justification.options) == 1
        assert justification.options[0].option == 'option'
        assert justification.options[0].required_image == True
        assert justification.options[0].required_text == True

        assert justification.selected_option == 'selected_option'
        assert justification.justification_text == 'text'
        assert justification.justification_image == 'image'
    
    def test_justification_dto_from_request_with_none_values(self):
        justification_dict = {
            'options': [
                {
                    'option': 'option',
                    'required_image': True,
                    'required_text': True
                }
            ],
            'selected_option': None,
            'justification_text': None,
            'justification_image': None
        }

        justification = JustificationDTO.from_request(justification_dict)

        assert len(justification.options) == 1
        assert justification.options[0].option == 'option'
        assert justification.options[0].required_image == True
        assert justification.options[0].required_text == True

        assert justification.selected_option == None
        assert justification.justification_text == None
        assert justification.justification_image == None
    
    def test_justification_dto_from_request_with_no_options(self):
        justification_dict = {
            'selected_option': 'selected_option',
            'justification_text': 'text',
            'justification_image': 'image'
        }

        with pytest.raises(EntityError):
            JustificationDTO.from_request(justification_dict)
    
    def test_justification_dto_from_request_with_no_option(self):
        justification_dict = {
            'options': [
                {
                    'required_image': True,
                    'required_text': True
                }
            ],
            'selected_option': 'selected_option',
            'justification_text': 'text',
            'justification_image': 'image'
        }

        with pytest.raises(EntityError):
            JustificationDTO.from_request(justification_dict)
    
    def test_justification_dto_from_request_with_no_required_image(self):
        justification_dict = {
            'options': [
                {
                    'option': 'option',
                    'required_text': True
                }
            ],
            'selected_option': 'selected_option',
            'justification_text': 'text',
            'justification_image': 'image'
        }

        with pytest.raises(EntityError):
            JustificationDTO.from_request(justification_dict)
    
    def test_justification_dto_to_entity(self):
        justification_dto = JustificationDTO(
                options=[
                    JustificationOption(
                        option='option',
                        required_image=True,
                        required_text=True
                    ),
                    JustificationOption(
                        option='option',
                        required_image=True,
                        required_text=True
                    )
                ],
                selected_option='selected_option',
                justification_text='text',
                justification_image='image'
        )

        justification = justification_dto.to_entity()

        assert len(justification.options) == 2
        assert justification.options[0].option == 'option'
        assert justification.options[0].required_image == True
        assert justification.options[0].required_text == True

        assert justification.selected_option == 'selected_option'
        assert justification.justification_text == 'text'
        assert justification.justification_image == 'image'
    
    def test_justification_dto_from_request_with_no_required_image(self):
        justification_dict = {
            'options': [
                {
                    'option': 'option',
                    'required_text': True
                }
            ],
            'selected_option': 'selected_option',
            'text': 'text',
            'image': 'image'
        }

        with pytest.raises(EntityError):
            JustificationDTO.from_request(justification_dict)
    
    def test_justification_dto_to_entity(self):
        justification_dto = JustificationDTO(
                options=[
                    JustificationOption(
                        option='option',
                        required_image=True,
                        required_text=True
                    ),
                    JustificationOption(
                        option='option',
                        required_image=True,
                        required_text=True
                    )
                ],
                selected_option='selected_option',
                justification_text='text',
                justification_image='image'
        )

        justification = justification_dto.to_entity()

        assert len(justification.options) == 2
        assert justification.options[0].option == 'option'
        assert justification.options[0].required_image == True
        assert justification.options[0].required_text == True

        assert justification.selected_option == 'selected_option'
        assert justification.justification_text == 'text'
        assert justification.justification_image == 'image'