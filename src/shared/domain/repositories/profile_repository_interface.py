from abc import ABC, abstractmethod
from typing import List, Optional

from src.shared.domain.entities.profile import Profile
from src.shared.domain.enums.role_enum import ROLE


class IProfileRepository(ABC):

    @abstractmethod
    def create_profile(self, profile: Profile) -> Profile:
        pass
    
    @abstractmethod
    def get_all_profiles(self) -> List[Profile]:
        pass

    @abstractmethod
    def update_profile(self, profile_id: str, new_role: Optional[ROLE] = None, systems_to_include: Optional[List[str]] = None, systems_to_exclude: Optional[List[str]] = None, new_enabled: Optional[bool] = None) -> Profile:
        pass

    @abstractmethod
    def get_profile_by_id(self, profile_id: str) -> Optional[Profile]:
        pass