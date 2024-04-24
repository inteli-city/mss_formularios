from typing import List
from src.shared.domain.entities.profile import Profile
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.profile_repository_interface import IProfileRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class LoginProfileUsecase:

    def __init__(self, repo: IProfileRepository):
        self.repo = repo
    
    def __call__(self, requester_user_id: str, name: str, email: str, systems: List[str]) -> Profile:
        profile = self.repo.get_profile_by_id(requester_user_id)

        if profile is not None:
            if not profile.enabled:
                raise ForbiddenAction("Usuário desabilitado")
            return profile
        
        profile = Profile(
            profile_id=requester_user_id,
            name=name,
            email=email,
            role=ROLE.FILLER,
            systems=systems,
            enabled=True
        )

        return self.repo.create_profile(profile=profile)