from datetime import datetime

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer

from app.core.db import Base


class ProjectDonation(Base):
    """Миксин для моделей CharityProject и Donation."""

    __abstract__ = True

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)

    __table_args__ = (
        CheckConstraint('full_amount > 0', name='check_full_amount_positive'),
        CheckConstraint(
            'invested_amount <= full_amount',
            name='check_full_amount_more_invested_amount'
        ),
        CheckConstraint(
            'invested_amount >= 0',
            name='check_invested_amount_positive'
        ),
    )

    def __repr__(self) -> str:
        return (
            f'{self.full_amount=}, {self.invested_amount=},'
            f' {self.create_date=}, {self.close_date=}'
        )
