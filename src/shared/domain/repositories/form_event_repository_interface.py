from abc import ABC, abstractmethod

from src.shared.domain.entities.form_event import FormEvent


class IFormEventRepository(ABC):

    @abstractmethod
    def create_event(self, event: FormEvent) -> FormEvent:
        pass
