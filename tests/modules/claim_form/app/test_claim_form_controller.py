from src.modules.claim_form.app.claim_form_controller import ClaimFormController
from src.modules.claim_form.app.claim_form_usecase import ClaimFormUsecase
from src.shared.domain.entities.field import TextField
from src.shared.domain.entities.form import Form
from src.shared.domain.entities.justification import Justification, JustificationOption, SelectedJustification
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.form_status_enum import FormStatus
from src.shared.domain.enums.priority_enum import Priority
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.form_event_repository_mock import FormEventRepositoryMock
from src.shared.infra.repositories.form_repository_mock import FormRepositoryMock

REQUESTER_ID = 'd61dbf66-a10f-11ed-a8fc-0242ac120099'
POOL_FORM_ID = 'd61dbf66-a10f-11ed-a8fc-0242ac120030'

justification_option = JustificationOption(option='option', required_image=True, required_text=True)
justification = Justification(
    options=[justification_option],
    selected=SelectedJustification(option='option', text='text', image_url='image'),
)


def _pool_form() -> Form:
    text_field = TextField(label='label', required=True, key='key', order=1, max_length=10, value='value')
    section = Section(section_id=1, fields=[text_field])
    return Form(
        id=POOL_FORM_ID, form_title='FORM TITLE', created_by=REQUESTER_ID, user_id=None,
        system='UBERLANDIA', street='1', city='1', latitude=1.0, longitude=1.0,
        priority=Priority.EMERGENCY, status=FormStatus.PENDING, created_at=1, updated_at=1,
        justification=justification, sections=[section],
    )


def _request(form_id: str, sub: str = REQUESTER_ID, groups: str = "FORMULARIOS,UBERLANDIA"):
    return HttpRequest(body={
        "requester_user": {"sub": sub, "name": "Tester", "email": "tester@example.com", "cognito:groups": groups},
        "form_id": form_id,
    })


class TestClaimFormController:
    def setup_method(self):
        self.form_repo = FormRepositoryMock()
        self.form_repo.forms.append(_pool_form())
        self.controller = ClaimFormController(ClaimFormUsecase(self.form_repo, FormEventRepositoryMock()))

    def test_claim_success_returns_200(self):
        response = self.controller(_request(POOL_FORM_ID))
        assert response.status_code == 200
        assert response.body["user_id"] == REQUESTER_ID
        assert response.body["possession"] == "OWNED"

    def test_claim_not_found_returns_404(self):
        response = self.controller(_request("00000000-0000-0000-0000-000000000000"))
        assert response.status_code == 404

    def test_claim_wrong_system_returns_403(self):
        response = self.controller(_request(POOL_FORM_ID, groups="FORMULARIOS,GAIA"))
        assert response.status_code == 403

    def test_claim_conflict_returns_409(self):
        self.controller(_request(POOL_FORM_ID))
        response = self.controller(_request(POOL_FORM_ID, sub='d61dbf66-a10f-11ed-a8fc-0242ac120098'))
        assert response.status_code == 409
