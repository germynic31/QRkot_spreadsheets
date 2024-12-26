# QRKot - Благотворительный фонд поддержки котиков

## Как запустить проект

#### Склонировать репозиторий и перейти в директорию проекта:

```bash
git clone https://github.com/germynic31/cat_charity_fund.git
cd cat_charity_fund
```

#### Создать виртуальное окружение и установить зависимости:
```bash
python3 -m venv venv
. venv\bin\activate
pip install -r requirements.txt
```

#### Заполнить .env

```bash
sudo nano .env
```

#### Пример:
```dotenv
API_APP_TITLE=Благотворительный фонд поддержки котиков
API_DATABASE_URL=sqlite+aiosqlite:///./db_name.db
API_SECRET=secret

# для google api
API_TYPE=service_account
API_PROJECT_ID=idid
API_PRIVATE_KEY_ID="1337qwerty"
API_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n1337qwerty\n-----END PRIVATE KEY-----\n"
API_CLIENT_EMAIL=project@qwerty11.iam.gserviceaccount.com
API_CLIENT_ID=1234567890
API_AUTH_URI=https://accounts.google.com/o/oauth2/auth
API_TOKEN_URI=https://oauth2.googleapis.com/token
API_AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
API_CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/project@qwerty11.iam.gserviceaccount.com
API_UNIVERSE_DOMAIN=googleapis.com
API_EMAIL=you_email@gmail.com
```

#### Выполнить миграции:

```bash
alembic upgrade head
```

#### Запустить приложение:
```bash
uvicorn app.main:app --reload
```

---


### Документация находится по адресу [Swagger](http://127.0.0.1:8000/docs) или [ReDoc](http://127.0.0.1:8000/redoc)

---

#### Авторы: [Герман Деев](https://github.com/germynic31), [Yandex-Practicum](https://github.com/Yandex-Practicum)

---

Проект создан в учебных целях на курсе Я.Практикума


