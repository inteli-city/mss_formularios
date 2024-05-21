import pytest
from src.shared.domain.entities.justificative import Justificative, JustificativeOption
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Justificative:

    option = JustificativeOption(option='option', requiredImage=True, requiredText=True)
    
    def test_justificative_option(self):
        option = JustificativeOption(option='option', requiredImage=True, requiredText=True)

        assert option.option == 'option'
        assert option.requiredImage == True
        assert option.requiredText == True
    
    def test_justificative_option_is_not_str(self):
        with pytest.raises(EntityError):
            JustificativeOption(option=1, requiredImage=True, requiredText=True)
    
    def test_justificative_option_required_image_is_not_bool(self):
        with pytest.raises(EntityError):
            JustificativeOption(option='option', requiredImage='True', requiredText=True)
    
    def test_justificative_option_required_text_is_not_bool(self):
        with pytest.raises(EntityError):
            JustificativeOption(option='option', requiredImage=True, requiredText='True')
    
    def test_justificative(self):
        justificative = Justificative(options=[self.option], selectedOption='option', text='text', image='image')

        assert justificative.options == [self.option]
        assert justificative.selectedOption == 'option'
        assert justificative.text == 'text'
        assert justificative.image == 'image'
    
    def test_justificative_options_is_not_list(self):
        with pytest.raises(EntityError):
            Justificative(options=self.option, selectedOption='option', text='text', image='image')
    
    def test_justificative_options_is_not_justificative_option(self):
        with pytest.raises(EntityError):
            Justificative(options=['option'], selectedOption='option', text='text', image='image')
    
    def test_justificative_selected_option_is_not_str(self):
        with pytest.raises(EntityError):
            Justificative(options=[self.option], selectedOption=1, text='text', image='image')
    
    def test_justificative_text_is_not_str(self):
        with pytest.raises(EntityError):
            Justificative(options=[self.option], selectedOption='option', text=1, image='image')

    def test_justificative_image_is_not_str(self):
        with pytest.raises(EntityError):
            Justificative(options=[self.option], selectedOption='option', text='text', image=1)
    
    def test_justificative_selected_option_is_none(self):
        justificative = Justificative(options=[self.option], selectedOption=None, text='text', image='image')

        assert justificative.selectedOption == None
    
    def test_justificative_text_is_none(self):
        justificative = Justificative(options=[self.option], selectedOption='option', text=None, image='image')

        assert justificative.text == None

    def test_justificative_image_is_none(self):
        justificative = Justificative(options=[self.option], selectedOption='option', text='text', image=None)

        assert justificative.image == None