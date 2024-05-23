from src.shared.domain.entities.form import Form
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.repositories.form_repository_interface import IFormRepository
from src.shared.environments import Environments
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class FormRepositoryDynamo(IFormRepository):

    @staticmethod
    def form_partition_key_format(user_id: str) -> str:
        return f'{user_id}'
    
    @staticmethod
    def form_sort_key_format(form_id: str) -> str:
        return f'form#{form_id}'

    def __init__(self):
        self.dynamo = DynamoDatasource(
            endpoint_url=Environments.get_envs().endpoint_url,
            dynamo_table_name=Environments.get_envs().dynamo_table_name,
            region=Environments.get_envs().region,
            partition_key=Environments.get_envs().dynamo_partition_key,
            sort_key=Environments.get_envs().dynamo_sort_key,
        )

    def get_form_by_user_id(self, user_id: str) -> dict:
        pass

    def create_form(self, form: Form) -> Form:
        pass
    
    def update_form_status(self, form_id: str, status: FORM_STATUS) -> Form:
        pass