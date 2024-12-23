from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.mixins import ProjectDonationMixin


class Donation(ProjectDonationMixin):
    """Модель для пожертвований."""
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)

    def __str__(self) -> str:
        return (
            f'{self.comment if self.comment else super.__str__(self)}, '
            f'Сумма пожертвования: {self.full_amount}'
        )
