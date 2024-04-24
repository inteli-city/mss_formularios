from src.shared.domain.entities.profile import Profile
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.profile_repository_mock import ProfileRepositoryMock


class Test_ProfileRepositoryMock:

    def test_get_profile_by_id(self):
        repo = ProfileRepositoryMock()
        profile = repo.get_profile_by_id('d61dbf66-a10f-11ed-a8fc-0242ac120001')

        assert profile.profile_id == 'd61dbf66-a10f-11ed-a8fc-0242ac120001'
        assert profile.name == 'Gabriel Godoy'
        assert profile.email == 'gabriel@hotmail.com'
        assert profile.role == ROLE.FILLER
        assert profile.systems == ['GAIA', 'JUNDIAI', 'FORMULARIOS']
    
    def test_get_all_profiles(self):
        repo = ProfileRepositoryMock()
        profiles = repo.get_all_profiles()

        assert len(profiles) == 3
        assert profiles[0].profile_id == 'd61dbf66-a10f-11ed-a8fc-0242ac120001'
    
    def test_create_profile(self):
        repo = ProfileRepositoryMock()
        profile_to_create = Profile(
            profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120004',
            name='Gabriel Godoy',
            email='gabriel.godoy@hotmail.com',
            role=ROLE.COORDINATOR,
            systems=['GAIA', 'JUNDIAI', 'FORMULARIOS']
        )

        profile = repo.create_profile(profile_to_create)

        assert profile.profile_id == 'd61dbf66-a10f-11ed-a8fc-0242ac120004'
        assert profile.name == 'Gabriel Godoy'
        assert profile.email == 'gabriel.godoy@hotmail.com'
        assert profile.role == ROLE.COORDINATOR
        assert profile.systems == ['GAIA', 'JUNDIAI', 'FORMULARIOS']
    
    def test_update_profile(self):
        repo = ProfileRepositoryMock()
        profile_to_update = {
            'name': 'Gabriel',
            'email': 'gabriel_update@gmail.com',
            'role': ROLE.COORDINATOR,
            'systems': ['FORMULARIOS'],
        }

        profile = repo.update_profile('d61dbf66-a10f-11ed-a8fc-0242ac120001', profile_to_update)

        assert profile.profile_id == 'd61dbf66-a10f-11ed-a8fc-0242ac120001'
        assert profile.name == 'Gabriel'
        assert profile.email == 'gabriel_update@gmail.com'
        assert profile.role == ROLE.COORDINATOR
        assert profile.systems == ['FORMULARIOS']


        