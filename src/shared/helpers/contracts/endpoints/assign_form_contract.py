from src.shared.helpers.contracts.base import RequestContractModel
from src.shared.helpers.contracts.schemas.form import FormResponseSchema


class AssignFormRequestSchema(RequestContractModel):
    user_id: str


class AssignFormResponseSchema(FormResponseSchema):
    pass
