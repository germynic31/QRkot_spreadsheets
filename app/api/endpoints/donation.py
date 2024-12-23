from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.constants import MY_DONATION_URL, USER_ID
from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import Donation, User
from app.schemas.donation import DonationCreate, DonationDB
from app.services.investment import invest


router = APIRouter()


@router.post(
    '/',
    response_model=DonationDB,
    response_model_exclude_defaults=True,
    response_model_exclude={USER_ID},
    dependencies=[Depends(current_user)],
    summary='Создает пожертвование.'
)
async def create_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
) -> Donation:
    donation: Donation = await donation_crud.create(donation, session, user)
    await invest(donation=donation, session=session)
    return donation


@router.get(
    '/',
    response_model=list[DonationDB],
    dependencies=[Depends(current_superuser)],
    summary='Выводит все пожертвования пользователей.'
)
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session),
) -> list[Donation]:
    return await donation_crud.get_multi(session)


@router.get(
    MY_DONATION_URL,
    response_model=list[DonationDB],
    response_model_exclude_defaults=True,
    response_model_exclude={USER_ID},
    dependencies=[Depends(current_user)],
    summary='Выводит все пожертвования пользователя.'
)
async def get_all_my_donations(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
) -> list[Donation]:
    return await donation_crud.get_multi(session, user)
