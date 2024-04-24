import abc
import re
from typing import List

from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError


class Profile(abc.ABC):
    profile_id: str
    email: str
    name: str
    role: ROLE
    systems: List[str]

    MIN_NAME_LENGTH = 2
    PROFILE_ID_LENGTH = 36

    def __init__(self, profile_id: str, email: str, name: str, role: ROLE, systems: List[str]):
        if not Profile.validate_profile_id(profile_id):
            raise EntityError("profile_id")
        self.user_id = profile_id

        if not Profile.validate_email(email):
            raise EntityError("email")
        self.email = email

        if not Profile.validate_name(name):
            raise EntityError("name")
        self.name = name

        if type(role) != ROLE:
            raise EntityError("role")
        self.role = role

        if type(systems) != list:
            raise EntityError("systems")
        if not systems:
            raise EntityError("systems")
        if not all(isinstance(system, str) for system in systems):
            raise EntityError("systems")
        self.systems = systems
        
        
    @staticmethod
    def validate_profile_id(profile_id: str) -> bool:
        if type(profile_id) != str:
            return False
        if len(profile_id) != Profile.PROFILE_ID_LENGTH:
            return False
        return True

    @staticmethod
    def validate_email(email) -> bool:
        if email == None:
            return False
        elif type(email) != str:
            return False

        regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        return bool(re.fullmatch(regex, email))

    @staticmethod
    def validate_name(name: str) -> bool:
        regex = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$")

        if name is None:
            return False
        elif type(name) != str:
            return False
        elif len(name) <= Profile.MIN_NAME_LENGTH:
            return False
        
        return bool(re.fullmatch(regex, name))