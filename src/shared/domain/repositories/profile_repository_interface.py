from abc import ABC, abstractmethod
from typing import List, Optional

from src.shared.domain.entities.profile import Profile


class IProfileRepository(ABC):

    @abstractmethod
    def create_profile(self, profile: Profile) -> Profile:
        pass
    
    @abstractmethod
    def get_all_profiles(self) -> List[Profile]:
        pass

    @abstractmethod
    def update_profile(self, profile_id: str, new_profile_data: dict) -> Profile:
        pass

    @abstractmethod
    def get_profile_by_id(self, profile_id: str) -> Optional[Profile]:
        pass