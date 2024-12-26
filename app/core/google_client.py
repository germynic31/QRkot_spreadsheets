from typing import AsyncGenerator

from aiogoogle import Aiogoogle
from aiogoogle.auth.creds import ServiceAccountCreds

from app.core.constants import INFO, SCOPES


cred = ServiceAccountCreds(scopes=SCOPES, **INFO)


async def get_service() -> AsyncGenerator[Aiogoogle]:
    async with Aiogoogle(service_account_creds=cred) as aiogoogle:
        yield aiogoogle
