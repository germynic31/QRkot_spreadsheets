from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


class DonationBase(BaseModel):
    """Базовая схема для пожертвований."""
    comment: Optional[str]
    full_amount: PositiveInt


class DonationCreate(DonationBase):
    """Схема для создания пожертвований."""


class DonationDB(DonationBase):
    """Схема пожертвований для базы данных."""
    id: int
    user_id: int
    create_date: datetime = Field(default_factory=datetime.now)
    close_date: Optional[datetime]
    fully_invested: bool = False
    invested_amount: int = 0

    class Config:
        orm_mode = True
