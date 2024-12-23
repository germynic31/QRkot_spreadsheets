from fastapi import APIRouter

from app.api.endpoints import (donation_router, google_api_router,
                               project_router, user_router)
from app.core.constants import PREFIX_DONATION_URL, PREFIX_PROJECT_URL


main_router = APIRouter()

main_router.include_router(
    project_router, prefix=PREFIX_PROJECT_URL, tags=['Charity projects']
)
main_router.include_router(
    donation_router, prefix=PREFIX_DONATION_URL, tags=['Donations']
)
main_router.include_router(
    google_api_router, prefix='/google', tags=['Google']
)
main_router.include_router(user_router)
