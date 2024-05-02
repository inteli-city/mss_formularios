from src.shared.domain.entities.profile import Profile
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.dtos.profile_dynamo_dto import ProfileDynamoDTO


class Test_ProfileDynamoDTO:

    def test_profile_dynamo_dto_from_entity(self):
        profile = Profile(
            profile_id='75648hbr-184n-1985-91han-7ghn4HgF182',
            email='email@email.com',
            name='name',
            role=ROLE.FILLER,
            systems=['systems'],
            enabled=True
        )

        profile_dto = ProfileDynamoDTO.from_entity(profile)

        assert profile_dto.profile_id == '75648hbr-184n-1985-91han-7ghn4HgF182'
        assert profile_dto.email == 'email@email.com'
        assert profile_dto.name == 'name'
        assert profile_dto.role == ROLE.FILLER
        assert profile_dto.systems == ['systems']
        assert profile_dto.enabled == True

    def test_profile_dynamo_dto_to_dynamo(self):
        profile_dto = ProfileDynamoDTO(
            profile_id='75648hbr-184n-1985-91han-7ghn4HgF182',
            email='email@email.com',
            name='name',
            role=ROLE.FILLER,
            systems=['systems'],
            enabled=True
        )

        expected_data = {
            'profile_id': '75648hbr-184n-1985-91han-7ghn4HgF182',
            'email': 'email@email.com',
            'name': 'name',
            'role': 'FILLER',
            'systems': ['systems'],
            'enabled': True
        }

        assert profile_dto.to_dynamo() == expected_data
    
    def test_profile_dynamo_dto_from_dynamo(self):
        profile_data = {
            'profile_id': '75648hbr-184n-1985-91han-7ghn4HgF182',
            'email': 'email@email.com',
            'name': 'name',
            'role': 'FILLER',
            'systems': ['systems'],
            'enabled': True
        }

        profile_dto = ProfileDynamoDTO.from_dynamo(profile_data)

        assert profile_dto.profile_id == '75648hbr-184n-1985-91han-7ghn4HgF182'
        assert profile_dto.email == 'email@email.com'
        assert profile_dto.name == 'name'
        assert profile_dto.role == ROLE.FILLER
        assert profile_dto.systems == ['systems']
        assert profile_dto.enabled == True
    
    def test_profile_dynamo_dto_to_entity(self):
        profile_dto = ProfileDynamoDTO(
            profile_id='75648hbr-184n-1985-91han-7ghn4HgF182',
            email='email@email.com',
            name='name',
            role=ROLE.FILLER,
            systems=['systems'],
            enabled=True
        )

        profile = profile_dto.to_entity()

        assert profile.profile_id == '75648hbr-184n-1985-91han-7ghn4HgF182'
        assert profile.email == 'email@email.com'
        assert profile.name == 'name'
        assert profile.role == ROLE.FILLER
        assert profile.systems == ['systems']
        assert profile.enabled == True