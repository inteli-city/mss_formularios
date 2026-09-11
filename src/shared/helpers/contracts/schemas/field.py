from typing import Literal

from pydantic import ConfigDict, Field

from src.shared.helpers.contracts.base import RequestContractModel

FieldTypeLiteral = Literal[
    "TEXT_FIELD",
    "NUMBER_FIELD",
    "DROPDOWN_FIELD",
    "TYPEAHEAD_FIELD",
    "RADIO_GROUP_FIELD",
    "DATE_FIELD",
    "CHECKBOX_FIELD",
    "CHECKBOX_GROUP_FIELD",
    "SWITCH_BUTTON_FIELD",
    "FILE_FIELD",
]


class GenericFieldSchema(RequestContractModel):
    model_config = ConfigDict(extra="allow")

    field_type: FieldTypeLiteral = Field(
        description="Tipo do campo — cada valor tem seus próprios campos extras "
        "obrigatórios (ex.: FILE_FIELD exige file_type/min_quantity/max_quantity; "
        "DROPDOWN_FIELD/TYPEAHEAD_FIELD/RADIO_GROUP_FIELD/CHECKBOX_GROUP_FIELD exigem options)."
    )
    label: str
    required: bool
    key: str
    order: int
    help_text: str | None = None
