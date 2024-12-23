from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """Схема для вывода данных пользователя."""


class UserCreate(schemas.BaseUserCreate):
    """Схема для создания нового пользователя."""


class UserUpdate(schemas.BaseUserUpdate):
    """Схема для редактирования существующего пользователя."""
