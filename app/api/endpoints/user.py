from fastapi import APIRouter

from app.core.constants import (AUTH_TAG_URL, JWT_URL, PREFIX_AUTH_URL,
                                PREFIX_USERS_URL, USER_TAG_URL)
from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate


router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix=JWT_URL,
    tags=[AUTH_TAG_URL],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix=PREFIX_AUTH_URL,
    tags=[AUTH_TAG_URL],
)
users_router = fastapi_users.get_users_router(UserRead, UserUpdate)
users_router.routes = [
    rout for rout in users_router.routes if rout.name != 'users:delete_user'
]
router.include_router(
    users_router,
    prefix=PREFIX_USERS_URL,
    tags=[USER_TAG_URL],
)
