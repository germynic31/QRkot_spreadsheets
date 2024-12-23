from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation, User


class CRUDDonation(CRUDBase):

    async def get_donation_for_user(
            self,
            user: User,
            session: AsyncSession,
    ) -> Optional[list[Donation]]:
        donations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return donations.scalars().all()

    async def get_free_donations(
            self,
            session: AsyncSession,
    ) -> Optional[list[Donation]]:
        free_donations = await session.execute(
            select(Donation).where(
                Donation.fully_invested == 0
            ).order_by(
                Donation.create_date
            )
        )
        return free_donations.scalars().all()


donation_crud = CRUDDonation(Donation)
