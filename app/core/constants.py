from app.core.config import settings


AUTH_TAG_URL: str = 'auth'
"""Тег для ссылок авторизации."""

USER_TAG_URL: str = 'users'
"""Тег для ссылок пользователей."""

MY_DONATION_URL: str = '/my'
"""Адрес пожертвований пользователя."""

PROJECTS_URL: str = '/{project_id}'
"""Адрес проекта (удаление и обновление)."""

PREFIX_DONATION_URL: str = '/donation'
"""Префикс для ссылок пожертвований."""

PREFIX_PROJECT_URL: str = '/charity_project'
"""Префикс для ссылок проектов."""

PREFIX_AUTH_URL: str = f'/{AUTH_TAG_URL}'
"""Префикс для ссылок авторизации."""

PREFIX_USERS_URL: str = f'/{USER_TAG_URL}'
"""Префикс для ссылок пользователей."""

JWT_URL: str = f'{PREFIX_AUTH_URL}/jwt'
"""Адрес для входа и выхода по JWT токену."""

USER_ID: str = 'user_id'
"""Поле user_id."""

MAX_LENGTH_NAME: int = 100
"""Максимальная длина названия проекта."""

MIN_LENGTH_NAME_AND_DESCRIPTION: int = 1
"""Минимальная длина имени и описания проекта."""

SCOPES: list = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
"""Разрешенные ссылки для google api."""

INFO: dict = {
    'type': settings.type,
    'project_id': settings.project_id,
    'private_key_id': settings.private_key_id,
    'private_key': settings.private_key,
    'client_email': settings.client_email,
    'client_id': settings.client_id,
    'auth_uri': settings.auth_uri,
    'token_uri': settings.token_uri,
    'auth_provider_x509_cert_url': settings.auth_provider_x509_cert_url,
    'client_x509_cert_url': settings.client_x509_cert_url
}
"""Информация про аккаунт проекта."""

LABEL_OPEN_DAYS: str = 'open_days'
"""Название атрибута открытых дней для проекта."""

FORMAT: str = "%Y/%m/%d %H:%M:%S"
"""Формат даты для таблицы."""

ROW_COUNT: int = 100
"""Количество строк в таблице."""

COLUMN_COUNT: int = 100
"""Количество колонок в таблице."""

RANGE_IN_TABLE: str = 'A1:E30'
"""Допустимые поля в таблице."""

VALUE_INPUT_OPTION: str = 'USER_ENTERED'
"""Тип ввода значений в таблицу."""
