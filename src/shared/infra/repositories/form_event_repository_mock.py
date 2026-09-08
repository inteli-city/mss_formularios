from copy import deepcopy
from typing import List

from src.shared.domain.entities.form_event import FormEvent
from src.shared.domain.repositories.form_event_repository_interface import IFormEventRepository


class FormEventRepositoryMock(IFormEventRepository):

    def __init__(self):
        self.events: List[FormEvent] = []

    def create_event(self, event: FormEvent) -> FormEvent:
        self.events.append(deepcopy(event))
        return event
