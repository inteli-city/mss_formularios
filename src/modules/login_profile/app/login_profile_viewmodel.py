from typing import List

from src.shared.domain.entities.profile import Profile
from src.shared.domain.enums.role_enum import ROLE


class ProfileViewmodel:
    profile_id: str
    email: str
    name: str
    role: ROLE
    systems: List[str]
    enabled: bool

    def __init__(self, profile: Profile):
        self.profile_id = profile.profile_id
        self.email = profile.email
        self.name = profile.name
        self.role = profile.role
        self.systems = profile.systems
        self.enabled = profile.enabled
    
    def to_dict(self):
        return {
            "profile_id": self.profile_id,
            "email": self.email,
            "name": self.name,
            "role": self.role.value,
            "systems": self.systems,
            "enabled": self.enabled
        }

class LoginProfileViewmodel:
    profile: ProfileViewmodel

    def __init__(self, profile: Profile):
        self.profile = ProfileViewmodel(profile=profile)
    
    def to_dict(self):
        return {
            "profile": self.profile.to_dict(),
            'message': 'Login realizado com sucesso!'
        }