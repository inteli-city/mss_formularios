from typing import List, Optional
from src.shared.domain.entities.profile import Profile
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.profile_repository_interface import IProfileRepository


class ProfileRepositoryMock(IProfileRepository):
    profiles: List[Profile]

    def __init__(self):
        self.profiles = [
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120001', name='Gabriel Godoy', email="gabriel@hotmail.com", role=ROLE.COORDINATOR, systems=['GAIA', 'JUNDIAI'], enabled=True),
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120002', name='Gabriel Godoy', email="gabriel@gmail.com", role=ROLE.FILLER, systems=['GAIA', 'JUNDIAI'], enabled=True),
            Profile(profile_id='d61dbf66-a10f-11ed-a8fc-0242ac120003', name='Gabriel Godoy', email="gabriel@outlook.com", role=ROLE.COORDINATOR, systems=['GAIA', 'JUNDIAI'], enabled=False),
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

    def update_profile(self, profile_id: str, new_role: Optional[ROLE] = None, systems_to_include: Optional[List[str]] = None, systems_to_exclude: Optional[List[str]] = None, new_enabled: Optional[bool] = None) -> Profile:
        for profile in self.profiles:
            if profile.profile_id == profile_id:
                if new_role is not None:
                    profile.role = new_role
                if systems_to_include is not None:
                    profile.systems.extend(systems_to_include)
                if systems_to_exclude is not None:
                    for system in systems_to_exclude:
                        profile.systems.remove(system)
                if new_enabled is not None:
                    profile.enabled = new_enabled
                return profile
        return None