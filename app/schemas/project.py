from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt

from app.core.constants import MAX_LENGTH_NAME


class CharityProjectBase(BaseModel):
    """Базовая схема для проектов."""
    name: str = Field(
        ...,
        min_length=1,
        max_length=MAX_LENGTH_NAME
    )
    description: str = Field(
        ...,
        min_length=1
    )
    full_amount: PositiveInt = Field()


class CharityProjectCreate(CharityProjectBase):
    """Схема для создания проектов."""


class CharityProjectUpdate(BaseModel):
    """Схема для обновления проектов."""
    name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=100
    )
    description: Optional[str] = Field(
        None,
        min_length=1
    )
    full_amount: Optional[PositiveInt] = Field(None)

    class Config:
        extra = Extra.forbid


class CharityProjectDB(CharityProjectBase):
    """Схема проектов для базы данных."""
    id: int
    create_date: datetime = Field(default_factory=datetime.now)
    close_date: Optional[datetime]
    fully_invested: Optional[bool] = False
    invested_amount: int = 0

    class Config:
        orm_mode = True
