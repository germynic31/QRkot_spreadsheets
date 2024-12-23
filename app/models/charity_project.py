from sqlalchemy import Column, String, Text

from app.core.constants import MAX_LENGTH_NAME
from app.models.mixins import ProjectDonationMixin


class CharityProject(ProjectDonationMixin):
    """Модель для благотворительных проектов."""
    name = Column(String(MAX_LENGTH_NAME), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __str__(self) -> str:
        return (
            f'{self.name}, '
            f'Осталось собрать: {self.full_amount - self.invested_amount}'
        )
