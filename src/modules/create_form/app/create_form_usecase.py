from datetime import datetime
from typing import List, Optional
import uuid
from src.shared.domain.entities.form import Form
from src.shared.domain.entities.information_field import InformationField
from src.shared.domain.entities.section import Section
from src.shared.domain.enums.form_status_enum import FORM_STATUS
from src.shared.domain.enums.priority_enum import PRIORITY
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.form_repository_interface import IFormRepository
from src.shared.domain.repositories.profile_repository_interface import IProfileRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class CreateFormUsecase:
    def __init__(self, form_repo: IFormRepository, profile_repo: IProfileRepository):
        self.form_repo = form_repo
        self.profile_repo = profile_repo

    def __call__(self,
                    extern_form_id: str,
                    creator_user_id: str,
                    user_id: str,
                    coordinators_id: List[str],
                    vinculation_form_id: Optional[str],
                    template: str,
                    area: str,
                    system: str,
                    street: str,
                    city: str,
                    number: int,
                    latitude: float,
                    longitude: float,
                    region: str,
                    description: Optional[str],
                    priority: PRIORITY,
                    expiration_date: int,
                    comments: Optional[str],
                    sections: List[Section],
                    information_fields: Optional[List[InformationField]]
                 ) -> Form:
        
        profile = self.profile_repo.get_profile_by_id(creator_user_id)
        
        if profile is None:
            raise ForbiddenAction("Perfil não encontrado")
        
        if not profile.enabled:
            raise ForbiddenAction("Usuário desabilitado")
        
        if not system in profile.systems:
            raise ForbiddenAction("Usuário não tem permissão para criar formulário para esse sistema")

        form = Form(
            extern_form_id=extern_form_id,
            internal_form_id=str(uuid.uuid4()),
            creator_user_id=creator_user_id,
            user_id=user_id,
            coordinators_id=coordinators_id,
            vinculation_form_id=vinculation_form_id,
            template=template,
            area=area,
            system=system,
            street=street,
            city=city,
            number=number,
            latitude=latitude,
            longitude=longitude,
            region=region,
            description=description,
            priority=priority,
            status=FORM_STATUS.NOT_STARTED,
            expiration_date=expiration_date,
            creation_date=int(datetime.now().timestamp() * 1000),
            start_date=None,
            conclusion_date=None,
            justificative=None,
            comments=comments,
            sections=sections,
            information_fields=information_fields
        )

        return self.form_repo.create_form(form)