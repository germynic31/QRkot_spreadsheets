from app.core.config import settings


# Тег для ссылок авторизации.
AUTH_TAG_URL: str = 'auth'

# Тег для ссылок пользователей.
USER_TAG_URL: str = 'users'

# Адрес пожертвований пользователя.
MY_DONATION_URL: str = '/my'

# """Адрес проекта (удаление и обновление)."""
PROJECTS_URL: str = '/{project_id}'

# Префикс для ссылок пожертвований.
PREFIX_DONATION_URL: str = '/donation'

# Префикс для ссылок проектов.
PREFIX_PROJECT_URL: str = '/charity_project'

# Префикс для ссылок авторизации.
PREFIX_AUTH_URL: str = f'/{AUTH_TAG_URL}'

# Префикс для ссылок пользователей.
PREFIX_USERS_URL: str = f'/{USER_TAG_URL}'

# Адрес для входа и выхода по JWT токену.
JWT_URL: str = f'{PREFIX_AUTH_URL}/jwt'

# Поле user_id.
USER_ID: str = 'user_id'

# Максимальная длина названия проекта.
MAX_LENGTH_NAME: int = 100

# Разрешенные ссылки для google api.
SCOPES: list = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Информация про аккаунт проекта.
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

# Формат даты для таблицы.
FORMAT: str = '%Y/%m/%d %H:%M:%S'

# Количество строк в таблице.
ROW_COUNT: int = 100

# Количество колонок в таблице.
COLUMN_COUNT: int = 100

# Тип ввода значений в таблицу.
VALUE_INPUT_OPTION: str = 'USER_ENTERED'
