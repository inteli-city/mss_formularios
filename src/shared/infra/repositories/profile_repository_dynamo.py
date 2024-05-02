from src.shared.domain.entities.profile import Profile
from src.shared.domain.repositories.profile_repository_interface import IProfileRepository


class ProfileRepositoryDynamo(IProfileRepository):

    def create_profile(self, profile: Profile) -> Profile:
        pass