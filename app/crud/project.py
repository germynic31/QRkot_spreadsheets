from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.constants import LABEL_OPEN_DAYS
from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return db_project_id.scalars().first()

    async def get_open_projects(
            self,
            session: AsyncSession,
    ) -> Optional[list[CharityProject]]:
        open_projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested == 0
            ).order_by(
                CharityProject.create_date
            )
        )
        return open_projects.scalars().all()

    async def get_oldest_open_project(
            self,
            session: AsyncSession,
    ) -> Optional[CharityProject]:
        open_projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested == 0
            ).order_by(
                CharityProject.create_date
            )
        )
        return open_projects.scalars().first()

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> Optional[list[CharityProject]]:
        reservations = await session.execute(
            select(
                CharityProject.name,
                CharityProject.description,
                (
                    func.julianday(CharityProject.close_date) -
                    func.julianday(CharityProject.create_date)
                ).label(LABEL_OPEN_DAYS)
            ).where(
                CharityProject.fully_invested
            ).order_by(
                (
                    func.julianday(CharityProject.close_date) -
                    func.julianday(CharityProject.create_date)
                ).label(LABEL_OPEN_DAYS)
            )
        )
        reservations = reservations.all()
        return reservations


charity_project_crud = CRUDCharityProject(CharityProject)
