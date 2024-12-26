from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base_models import ProjectDonation


class Donation(ProjectDonation):
    """Модель для пожертвований."""

    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)

    def __repr__(self) -> str:
        return f'{self.user_id=}, {self.comment=}' + super.__repr__(self)
