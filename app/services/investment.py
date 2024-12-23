from datetime import datetime
from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.donation import donation_crud
from app.crud.project import charity_project_crud
from app.models import CharityProject, Donation


async def update_object(
        obj: Union[Donation, CharityProject],
        object_for_calculate: Union[Donation, CharityProject, None] = None
):
    """Обновляет объект при инвестировании."""
    if object_for_calculate:
        obj.invested_amount += (object_for_calculate.full_amount -
                                object_for_calculate.invested_amount)
    else:
        obj.invested_amount = obj.full_amount
    obj.fully_invested = True
    obj.close_date = datetime.now()


async def handle_investment(
        donation: Donation,
        project: CharityProject,
) -> None:
    """Управление инвестированиями."""
    donation_left = donation.full_amount - donation.invested_amount
    project_left = project.full_amount - project.invested_amount
    if donation_left > project_left:
        donation.invested_amount += project_left
        await update_object(project, project)

    if donation_left == project_left:
        await update_object(project, donation)
        await update_object(donation)

    if donation_left < project_left:
        project.invested_amount += donation_left
        await update_object(donation)


async def invest(
        *,
        project: CharityProject = None,
        donation: Donation = None,
        session: AsyncSession,
) -> None:
    """Основная функция инвестирования."""
    if project:
        free_donations = await donation_crud.get_free_donations(session)
        for donation in free_donations:
            await handle_investment(donation, project)
            await session.commit()
            await session.refresh(project)

    if donation:
        project = await charity_project_crud.get_oldest_open_project(session)
        if project:
            await handle_investment(donation, project)
            await session.commit()
            await session.refresh(donation)
