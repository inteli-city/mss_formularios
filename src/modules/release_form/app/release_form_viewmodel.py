from src.shared.domain.entities.form import Form
from src.shared.helpers.contracts.endpoints.release_form_contract import ReleaseFormResponseSchema
from src.shared.helpers.viewmodels.form_dict_builders import build_form_dict


class ReleaseFormViewmodel:
    def __init__(self, form: Form):
        self.form = form

    def to_dict(self) -> dict:
        payload = build_form_dict(self.form, include_dynamic_extras=True, expand_selected=True)
        return ReleaseFormResponseSchema.model_validate(payload).model_dump()
