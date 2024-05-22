import pytest
from src.shared.domain.entities.justificative import Justificative, JustificativeOption
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.dtos.justificative_dto import JustificativeDTO


class Test_JustificativeDTO:

    def test_justificative_dto_from_request(self):
        justificative_dict = {
            'options': [
                {
                    'option': 'option',
                    'required_image': True,
                    'required_text': True
                },
                {
                    'option': 'option',
                    'required_image': True,
                    'required_text': True
                }
            ],
            'selected_option': 'selected_option',
            'text': 'text',
            'image': 'image'
        }

        justificative = JustificativeDTO.from_request(justificative_dict)

        assert len(justificative.justificative.options) == 2
        assert justificative.justificative.options[0].option == 'option'
        assert justificative.justificative.options[0].required_image == True
        assert justificative.justificative.options[0].required_text == True

        assert justificative.justificative.selected_option == 'selected_option'
        assert justificative.justificative.text == 'text'
        assert justificative.justificative.image == 'image'
    
    def test_justificative_dto_from_request_with_none_values(self):
        justificative_dict = {
            'options': [
                {
                    'option': 'option',
                    'required_image': True,
                    'required_text': True
                },
                {
                    'option': 'option',
                    'required_image': True,
                    'required_text': True
                }
            ],
            'selected_option': None,
            'text': None,
            'image': None
        }

        justificative = JustificativeDTO.from_request(justificative_dict)

        assert len(justificative.justificative.options) == 2
        assert justificative.justificative.options[0].option == 'option'
        assert justificative.justificative.options[0].required_image == True
        assert justificative.justificative.options[0].required_text == True

        assert justificative.justificative.selected_option == None
        assert justificative.justificative.text == None
        assert justificative.justificative.image == None
    
    def test_justificative_dto_from_request_with_no_options(self):
        justificative_dict = {
            'selected_option': 'selected_option',
            'text': 'text',
            'image': 'image'
        }

        with pytest.raises(EntityError):
            JustificativeDTO.from_request(justificative_dict)
    
    def test_justificative_dto_from_request_with_no_option(self):
        justificative_dict = {
            'options': [
                {
                    'required_image': True,
                    'required_text': True
                }
            ],
            'selected_option': 'selected_option',
            'text': 'text',
            'image': 'image'
        }

        with pytest.raises(EntityError):
            JustificativeDTO.from_request(justificative_dict)
    
    def test_justificative_dto_from_request_with_no_required_image(self):
        justificative_dict = {
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
            JustificativeDTO.from_request(justificative_dict)
    
    def test_justificative_dto_to_entity(self):
        justificative_dto = JustificativeDTO(
            Justificative(
                options=[
                    JustificativeOption(
                        option='option',
                        required_image=True,
                        required_text=True
                    ),
                    JustificativeOption(
                        option='option',
                        required_image=True,
                        required_text=True
                    )
                ],
                selected_option='selected_option',
                text='text',
                image='image'
            )
        )

        justificative = justificative_dto.to_entity()

        assert len(justificative.options) == 2
        assert justificative.options[0].option == 'option'
        assert justificative.options[0].required_image == True
        assert justificative.options[0].required_text == True

        assert justificative.selected_option == 'selected_option'
        assert justificative.text == 'text'
        assert justificative.image == 'image'
    
    def test_justificative_dto_from_request_with_no_required_image(self):
        justificative_dict = {
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
            JustificativeDTO.from_request(justificative_dict)
    
    def test_justificative_dto_to_entity(self):
        justificative_dto = JustificativeDTO(
            Justificative(
                options=[
                    JustificativeOption(
                        option='option',
                        required_image=True,
                        required_text=True
                    ),
                    JustificativeOption(
                        option='option',
                        required_image=True,
                        required_text=True
                    )
                ],
                selected_option='selected_option',
                text='text',
                image='image'
            )
        )

        justificative = justificative_dto.to_entity()

        assert len(justificative.options) == 2
        assert justificative.options[0].option == 'option'
        assert justificative.options[0].required_image == True
        assert justificative.options[0].required_text == True

        assert justificative.selected_option == 'selected_option'
        assert justificative.text == 'text'
        assert justificative.image == 'image'