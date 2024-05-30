from typing import List, Optional
from src.shared.domain.entities.profile import Profile
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.profile_repository_interface import IProfileRepository
from src.shared.environments import Environments
from src.shared.infra.dtos.profile_dynamo_dto import ProfileDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class ProfileRepositoryDynamo(IProfileRepository):

    @staticmethod
    def profile_primary_key_format(profile_id: str) -> str:
        return f'{profile_id}'

    def __init__(self):
        self.dynamo = DynamoDatasource(
            dynamo_table_name=Environments.get_envs().dynamo_table_name_profile,
            region=Environments.get_envs().region,
            partition_key=Environments.get_envs().dynamo_partition_key,
            sort_key=Environments.get_envs().dynamo_sort_key,
        )

    def create_profile(self, profile: Profile) -> Profile:
        item = ProfileDynamoDTO.from_entity(profile).to_dynamo()
        resp = self.dynamo.put_item(item=item, partition_key=self.profile_primary_key_format(profile.profile_id), is_decimal=True)
        
        return profile
    
    def get_all_profiles(self) -> List[Profile]:

        response = self.dynamo.get_all_items()

        profiles = list()

        for item in response["Items"]:
            profiles.append(ProfileDynamoDTO.from_dynamo(item).to_entity())
        
        return profiles
    
    def update_profile(self, profile_id: str, new_role: Optional[ROLE] = None, systems_to_include: Optional[List[str]] = None, systems_to_exclude: Optional[List[str]] = None, new_enabled: Optional[bool] = None) -> Profile:
        profile_to_update = self.get_profile_by_id(profile_id=profile_id)

        if profile_to_update is None:
            return None
        
        if new_role is not None:
            profile_to_update.role = new_role
        if systems_to_include is not None:
            profile_to_update.systems += systems_to_include
        if systems_to_exclude is not None:
            profile_to_update.systems = [system for system in profile_to_update.systems if system not in systems_to_exclude]
        if new_enabled is not None:
            profile_to_update.enabled = new_enabled
        
        update_dict = ProfileDynamoDTO.from_entity(profile_to_update).to_dynamo()

        resp = self.dynamo.update_item(partition_key=self.profile_primary_key_format(profile_id=profile_to_update.profile_id), sort_key=None, update_dict=update_dict)

        if "Attributes" not in resp:
            return None
        
        return ProfileDynamoDTO.from_dynamo(resp["Attributes"]).to_entity()

    def get_profile_by_id(self, profile_id: str) -> Optional[Profile]:
        response = self.dynamo.get_item(partition_key=self.profile_primary_key_format(profile_id=profile_id))

        if "Item" not in response:
            return None
        
        return ProfileDynamoDTO.from_dynamo(response["Item"]).to_entity()