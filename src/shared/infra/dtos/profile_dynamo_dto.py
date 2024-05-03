from typing import List
from src.shared.domain.entities.profile import Profile
from src.shared.domain.enums.role_enum import ROLE


class ProfileDynamoDTO:
    profile_id: str
    email: str
    name: str
    role: ROLE
    systems: List[str]
    enabled: bool

    def __init__(self, profile_id: str, email: str, name: str, role: ROLE, systems: List[str], enabled: bool):
        self.profile_id = profile_id
        self.email = email
        self.name = name
        self.role = role
        self.systems = systems
        self.enabled = enabled
    
    @staticmethod
    def from_entity(profile: Profile) -> "ProfileDynamoDTO":
        return ProfileDynamoDTO(
            profile_id=profile.profile_id,
            email=profile.email,
            name=profile.name,
            role=profile.role,
            systems=profile.systems,
            enabled=profile.enabled
        )
    
    def to_dynamo(self) -> dict:
        data =  {
            'profile_id': self.profile_id,
            'email': self.email,
            'name': self.name,
            'role': self.role.value,
            'systems': self.systems,
            'enabled': self.enabled
        }

        data_without_none_values = {k: v for k, v in data.items() if v is not None}
        return data_without_none_values

    @staticmethod
    def from_dynamo(profile_data: dict) -> "ProfileDynamoDTO":
        return ProfileDynamoDTO(
            profile_id=profile_data['profile_id'],
            email=profile_data['email'],
            name=profile_data['name'],
            role=ROLE(profile_data['role']),
            systems=[system for system in profile_data['systems']],
            enabled=profile_data['enabled']
        )
    
    def to_entity(self) -> Profile:
        return Profile(
            profile_id=self.profile_id,
            email=self.email,
            name=self.name,
            role=self.role,
            systems=self.systems,
            enabled=self.enabled
        )
    
    def __repr__(self):
        return f"ProfileDynamoDTO(profile_id={self.profile_id}, email={self.email}, name={self.name}, role={self.role}, systems={self.systems}, enabled={self.enabled})"
    
    def __eq__(self, other):
         return self.profile_id == other.name and self.email == other.email and self.name == other.name and self.role == other.role and self.systems == other.systems and self.enabled == other.enabled