from src.modules.login_profile.app.login_profile_viewmodel import LoginProfileViewmodel, ProfileViewmodel
from src.shared.domain.entities.profile import Profile
from src.shared.domain.enums.role_enum import ROLE


class Test_LoginProfileViewmodel:

    def test_profile_viewmodel(self):
        profile = Profile(
            profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120001',
            name='Gabriel Godoy',
            email='gabriel@gmail.com',
            role=ROLE.COORDINATOR,
            systems=['GAIA', 'JUNDIAI', 'TEST'],
            enabled=True
        )

        viewmodel = ProfileViewmodel(profile=profile)

        excepted = {
            "profile_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
            "email": 'gabriel@gmail.com',
            "name": 'Gabriel Godoy',
            "role": 'COORDINATOR',
            "systems": ['GAIA', 'JUNDIAI', 'TEST'],
            "enabled": True
        }

        assert viewmodel.to_dict() == excepted
    
    def test_login_profile_viewmodel(self):
        profile = Profile(
            profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120001',
            name='Gabriel Godoy',
            email='gabriel@gmail.com',
            role=ROLE.COORDINATOR,
            systems=['GAIA', 'JUNDIAI', 'TEST'],
            enabled=True
        )

        viewmodel = LoginProfileViewmodel(profile=profile)

        excepted = {
                "profile": {
                "profile_id": 'd61dbf66-a10f-11ed-a8fc-0242ac120001',
                "email": 'gabriel@gmail.com',
                "name": 'Gabriel Godoy',
                "role": 'COORDINATOR',
                "systems": ['GAIA', 'JUNDIAI', 'TEST'],
                "enabled": True
            },
            'message': 'Login realizado com sucesso!'
        }

        assert viewmodel.to_dict() == excepted