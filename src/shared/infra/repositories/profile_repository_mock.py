from typing import List, Optional
from src.shared.domain.entities.profile import Profile
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.profile_repository_interface import IProfileRepository


class ProfileRepositoryMock(IProfileRepository):
    profiles: List[Profile]

    def __init__(self):
        self.profiles = [
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', name='Gabriel Godoy', email="gabriel@hotmail.com", role=ROLE.FILLER, systems=['GAIA', 'JUNDIAI', 'FORMULARIOS']),
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002', name='Gabriel Godoy', email="gabriel@gmail.com", role=ROLE.FILLER, systems=['GAIA', 'JUNDIAI', 'FORMULARIOS']),
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120003', name='Gabriel Godoy', email="gabriel@outlook.com", role=ROLE.COORDINATOR, systems=['GAIA', 'JUNDIAI', 'FORMULARIOS']),
        ]
    
    def get_profile_by_id(self, profile_id: str) -> Optional[Profile]:
        for profile in self.profiles:
            if profile_id == profile.profile_id:
                return profile
        return None
    
    def get_all_profiles(self) -> List[Profile]:
        if len(self.profiles) > 0:
            return self.profiles
        else:
            return None
    
    def create_profile(self, profile: Profile) -> Profile:
        self.profiles.append(profile)
        return profile

    def update_profile(self, profile_id: str, new_profile_data: dict) -> Profile:
        for index, profilex in enumerate(self.profiles):
            if profilex.profile_id == profile_id:
                for key, value in new_profile_data.items():
                    setattr(profilex, key, value)
                return profilex
        return None