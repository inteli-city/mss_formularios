from src.shared.domain.entities.form_event import FormEvent
from src.shared.domain.repositories.form_event_repository_interface import IFormEventRepository
from src.shared.environments import Environments
from src.shared.infra.dtos.form_event_dynamo_dto import FormEventDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class FormEventRepositoryDynamo(IFormEventRepository):
    """Mesma `Formularios_Table` do Form — sem tabela ou índice novo."""

    def __init__(self):
        envs = Environments.get_envs()
        self.dynamo = DynamoDatasource(
            endpoint_url=envs.endpoint_url,
            dynamo_table_name=envs.dynamo_table_name,
            region=envs.region,
            partition_key=envs.dynamo_partition_key,
            sort_key=envs.dynamo_sort_key,
        )

    def create_event(self, event: FormEvent) -> FormEvent:
        item = FormEventDynamoDTO.from_entity(event).to_dynamo()
        self.dynamo.put_item(
            item=item,
            partition_key=FormEventDynamoDTO.build_pk(event.form_id),
            sort_key=FormEventDynamoDTO.build_sk(event.created_at, event.id),
        )
        return event
