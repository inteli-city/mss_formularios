from typing import Dict, Any, List

from src.shared.domain.entities.field import Field
from src.shared.domain.entities.section import Section
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.infra.dtos.field_dto import FieldDTO

class SectionDTO:
    section_id: str
    fields: List[Field]
    
    def __init__(self, section_id: str, fields: List[Field]):
        self.section_id = section_id
        self.fields = fields
    
    def from_request(section_dict: dict) -> "SectionDTO":
        if 'section_id' not in section_dict:
            raise MissingParameters('section_id')
        section_id = section_dict['section_id']

        if 'fields' not in section_dict or not section_dict['fields']:
            raise MissingParameters('fields')
        fields_data = section_dict['fields']

        fields = [FieldDTO.from_dict(field_dict=field_data).to_entity() for field_data in fields_data]

        return SectionDTO(
            section_id=section_id,
            fields=fields
        )

    def to_dynamo(self) -> dict:
        dynamo_dict = {
            "section_id": self.section.section_id,
            "fields": [FieldDTO(field).to_dynamo() for field in self.section.fields]
        }
        return dynamo_dict

    def to_entity(self) -> Section:
        return Section(self.section_id, self.fields)
