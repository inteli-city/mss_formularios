import pytest
from src.shared.domain.entities.profile import Profile
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Profile:

    def test_profile(self):
        Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                    name='Gabriel Godoy',
                    email='gabriel.godoy@gmail.com',
                    role=ROLE.COORDINATOR,
                    systems=['GAIA', 'JUNDIAI', 'FORMULARIOS'],
                    enabled=True
                )
    
    def test_profile_id_is_none(self):
        with pytest.raises(EntityError):
            Profile(profile_id=None,
                 name='Gabriel Godoy',
                    email='gabriel.godoy@gmail.com',
                    role=ROLE.COORDINATOR,
                    systems=['GAIA', 'JUNDIAI', 'FORMULARIOS'],
                    enabled=True
                )
    
    def test_profile_id_is_not_str(self):
        with pytest.raises(EntityError):
            Profile(profile_id=1,
                 name='Gabriel Godoy',
                    email='gabriel.godoy@gmail.com',
                    role=ROLE.COORDINATOR,
                    systems=['GAIA', 'JUNDIAI', 'FORMULARIOS'],
                    enabled=True
                )
    
    def test_profile_id_not_minimun_length(self):
        with pytest.raises(EntityError):
            Profile(profile_id='123',
                        name='Gabriel Godoy',
                        email='gabriel.godoy@gmail.com',
                        role=ROLE.COORDINATOR,
                        systems=['GAIA', 'JUNDIAI', 'FORMULARIOS'],
                        enabled=True
                    )
    
    def test_profile_email_is_none(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name='Gabriel Godoy',
                    email=None,
                    role=ROLE.COORDINATOR,
                    systems=['GAIA', 'JUNDIAI', 'FORMULARIOS'],
                    enabled=True
                )
    
    def test_profile_email_is_not_str(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name='Gabriel Godoy',
                    email=1,
                    role=ROLE.COORDINATOR,
                    systems=['GAIA', 'JUNDIAI', 'FORMULARIOS'],
                    enabled=True
                )
    
    def test_profile_email_is_not_valid(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name='Gabriel Godoy',
                    email='gabriel',
                    role=ROLE.COORDINATOR,
                    systems=['GAIA', 'JUNDIAI', 'FORMULARIOS'],
                    enabled=True
                )
    
    def test_profile_name_is_none(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name=None,
                    email='gabriel.godoy@gmail.com',
                    role=ROLE.COORDINATOR,
                    systems=['GAIA', 'JUNDIAI', 'FORMULARIOS'],
                    enabled=True
                )
    
    def test_profile_name_is_not_str(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name=1,
                    email='gabriel.godoy@gmail.com',
                    role=ROLE.COORDINATOR,
                    systems=['GAIA', 'JUNDIAI', 'FORMULARIOS'],
                    enabled=True
                )
    
    def test_profile_name_is_not_minimun_length(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name='a',
                    email='gabriel.godoy@gmail.com',
                    role=ROLE.COORDINATOR,
                    systems=['GAIA', 'JUNDIAI', 'FORMULARIOS'],
                    enabled=True
                )
    
    def test_profile_name_is_not_valid(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name='Gabriel 122332',
                    email='gabriel.godoy@gmail.com',
                    role=ROLE.COORDINATOR,
                    systems=['GAIA', 'JUNDIAI', 'FORMULARIOS'],
                    enabled=True
                )
    
    def test_profile_role_is_none(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name='Gabriel Godoy',
                    email='gabriel.godoy@gmail.com',
                    role=None,
                    systems=['GAIA', 'JUNDIAI', 'FORMULARIOS'],
                    enabled=True
                )
    
    def test_profile_role_is_not_enum(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name='Gabriel Godoy',
                    email='gabriel.godoy@gmail.com',
                    role='ROLE.COORDINATOR',
                    systems=['GAIA', 'JUNDIAI', 'FORMULARIOS'],
                    enabled=True
                )
    
    def test_profile_systems_is_none(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name='Gabriel Godoy',
                 email='gabriel.godoy@gmail.com',
                    role='ROLE.COORDINATOR',
                    systems=None,
                    enabled=True
                )
    
    def test_profile_systems_is_empty(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name='Gabriel Godoy',
                 email='gabriel.godoy@gmail.com',
                    role='ROLE.COORDINATOR',
                    systems=[],
                    enabled=True
                )
    
    def test_profile_systems_is_list_is_not_str(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name='Gabriel Godoy',
                 email='gabriel.godoy@gmail.com',
                    role='ROLE.COORDINATOR',
                    systems=[1],
                    enabled=True
                )
    
    def test_profile_enabled_is_none(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name='Gabriel Godoy',
                 email='gabriel.godoy@gmail.com',
                    role='ROLE.COORDINATOR',
                    systems=[1],
                    enabled=None
                )
    
    def test_profile_enabled_is_not_bool(self):
        with pytest.raises(EntityError):
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002',
                 name='Gabriel Godoy',
                 email='gabriel.godoy@gmail.com',
                    role='ROLE.COORDINATOR',
                    systems=[1],
                    enabled='True'
                )