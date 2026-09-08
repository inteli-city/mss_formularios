import pytest

from src.modules.claim_form.app.claim_form_usecase import ClaimFormUsecase
from src.shared.domain.entities.field import TextField
from src.shared.domain.entities.form import Form
from src.shared.domain.entities.justification import Justification, JustificationOption, SelectedJustification
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.form_status_enum import FormStatus
from src.shared.domain.enums.priority_enum import Priority
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.form_event_repository_mock import FormEventRepositoryMock
from src.shared.infra.repositories.form_repository_mock import FormRepositoryMock

REQUESTER_ID = 'd61dbf66-a10f-11ed-a8fc-0242ac120099'
POOL_FORM_ID = 'd61dbf66-a10f-11ed-a8fc-0242ac120030'

justification_option = JustificationOption(option='option', required_image=True, required_text=True)
justification = Justification(
    options=[justification_option],
    selected=SelectedJustification(option='option', text='text', image_url='image'),
)


def _pool_form(**overrides) -> Form:
    text_field = TextField(label='label', required=True, key='key', order=1, max_length=10, value='value')
    section = Section(section_id=1, fields=[text_field])
    base = dict(
        id=POOL_FORM_ID, form_title='FORM TITLE', created_by=REQUESTER_ID, user_id=None,
        system='UBERLANDIA', street='1', city='1', latitude=1.0, longitude=1.0,
        priority=Priority.EMERGENCY, status=FormStatus.PENDING, created_at=1, updated_at=1,
        justification=justification, sections=[section],
    )
    base.update(overrides)
    return Form(**base)


class TestClaimFormUsecase:
    def setup_method(self):
        self.form_repo = FormRepositoryMock()
        self.form_event_repo = FormEventRepositoryMock()
        self.usecase = ClaimFormUsecase(self.form_repo, self.form_event_repo)

    def test_claim_success_records_event(self):
        self.form_repo.forms.append(_pool_form())

        form = self.usecase(requester_user_id=REQUESTER_ID, requester_systems=['UBERLANDIA'], form_id=POOL_FORM_ID)

        assert form.user_id == REQUESTER_ID
        assert form.possession.value == 'OWNED'
        assert len(self.form_event_repo.events) == 1
        assert self.form_event_repo.events[0].event_type.value == 'CLAIMED'
        assert self.form_event_repo.events[0].actor_user_id == REQUESTER_ID

    def test_claim_not_found_raises(self):
        with pytest.raises(NoItemsFound):
            self.usecase(requester_user_id=REQUESTER_ID, requester_systems=None, form_id='00000000-0000-0000-0000-000000000000')

    def test_claim_wrong_system_raises_forbidden(self):
        self.form_repo.forms.append(_pool_form())
        with pytest.raises(ForbiddenAction):
            self.usecase(requester_user_id=REQUESTER_ID, requester_systems=['GAIA'], form_id=POOL_FORM_ID)

    def test_claim_already_owned_raises_conflict(self):
        self.form_repo.forms.append(_pool_form(user_id='d61dbf66-a10f-11ed-a8fc-0242ac120001'))
        with pytest.raises(DuplicatedItem):
            self.usecase(requester_user_id=REQUESTER_ID, requester_systems=['UBERLANDIA'], form_id=POOL_FORM_ID)
