from sqlalchemy import Column, String, Text

from app.core.constants import MAX_LENGTH_NAME
from app.models.base_models import ProjectDonation


class CharityProject(ProjectDonation):
    """Модель для благотворительных проектов."""

    name = Column(String(MAX_LENGTH_NAME), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f'{self.name=}, {super().__repr__()}'
