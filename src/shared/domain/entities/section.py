import abc
from dataclasses import Field
from typing import List


class Section(abc.ABC):
    section_id: str
    fields: List[Field]
