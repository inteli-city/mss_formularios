from typing import List, Optional
from src.shared.domain.entities.form import Form
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.repositories.form_repository_interface import IFormRepository
from src.shared.environments import Environments
from src.shared.infra.dtos.form_dynamo_dto import FormDynamoDTO
from src.shared.infra.dtos.section_dto import SectionDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource
from boto3.dynamodb.conditions import Key

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
    
    def get_form_by_id(self, user_id: str, form_id: str) -> Form:
        form = self.dynamo.get_item(partition_key=self.form_partition_key_format(user_id), sort_key=self.form_sort_key_format(form_id))
        if "Item" not in form:
            return None

        return FormDynamoDTO.from_dynamo(form['Item']).to_entity()

    def get_form_by_user_id(self, user_id: str) -> dict:
        query_string = Key(self.dynamo.partition_key).eq(self.form_partition_key_format(user_id))
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES')

        forms = []

        for item in resp:
            forms.append(FormDynamoDTO.from_dynamo(item).to_entity())
        
        return forms

    def create_form(self, form: Form) -> Form:
        item = FormDynamoDTO.from_entity(form).to_dynamo()
        self.dynamo.put_item(item=item, partition_key=self.action_partition_key_format(form.user_id), sort_key=self.action_sort_key_format(form.form_id), is_decimal=True)
        
        return form
    
    def update_form_status(self, user_id: str, form_id: str, status: FORM_STATUS) -> Form:
        update_dict = {
            "status": status.value
        }

        resp = self.dynamo.update_item(partition_key=self.project_partition_key_format(user_id), sort_key=self.project_sort_key_format(form_id), update_dict=update_dict)
        
        if "Attributes" not in resp:
            return None
        
        return FormDynamoDTO.from_dynamo(resp['Attributes']).to_entity()
    
    def cancel_form(self, user_id: str, form_id: str, selected_option: str, justification_text: Optional[str] = None, justification_image: Optional[str] = None) -> Form:
        update_dict = {
            "status": FORM_STATUS.CANCELED.value,
            "justification": {
                "selected_option": selected_option,
                "justification_text": justification_text,
                "justification_image": justification_image
            }
        }

        resp = self.dynamo.update_item(partition_key=self.project_partition_key_format(user_id), sort_key=self.project_sort_key_format(form_id), update_dict=update_dict)
        
        if "Attributes" not in resp:
            return None
        
        return FormDynamoDTO.from_dynamo(resp['Attributes']).to_entity()
    
    def complete_form(self, user_id: str, form_id: str, sections: List[Section], vinculation_form_id: Optional[str] = None) -> Form:
        update_dict = {
            "status": FORM_STATUS.CONCLUDED.value,
            "sections": [
                SectionDTO.from_entity(section).to_dynamo() for section in sections
            ],
            "vinculation_form_id": vinculation_form_id
        }

        resp = self.dynamo.update_item(partition_key=self.project_partition_key_format(user_id), sort_key=self.project_sort_key_format(form_id), update_dict=update_dict)
        
        if "Attributes" not in resp:
            return None
        
        return FormDynamoDTO.from_dynamo(resp['Attributes']).to_entity()