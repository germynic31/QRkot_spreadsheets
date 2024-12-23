from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.project import charity_project_crud
from app.models import CharityProject
from app.schemas.project import CharityProjectUpdate


async def check_project_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    """Название проекта уникальное."""
    project_id: CharityProject or None = (
        await charity_project_crud.get_project_id_by_name(
            project_name,
            session
        )
    )
    if project_id:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проект с таким именем уже существует!',
        )


async def check_project_exists(
        project_id: int,
        session: AsyncSession,
) -> CharityProject:
    """Если проект существует, то он возвращается."""
    project: CharityProject = await charity_project_crud.get(
        project_id,
        session
    )
    if not project:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Проект не найден!'
        )
    return project


async def check_invested_for_delete(
        project_id: int,
        session: AsyncSession,
) -> None:
    """Инвестированные средства меньше требуемой суммы."""
    project: CharityProject = await charity_project_crud.get(
        project_id,
        session
    )
    if project.invested_amount > 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=(
                'Нельзя удалить проект,'
                ' в который уже были инвестированы средства,'
                ' его можно только закрыть!'
            )
        )


async def check_update_on_close_project(
        project_id: int,
        session: AsyncSession,
) -> None:
    """Закрыт ли проект."""
    project: CharityProject = await charity_project_crud.get(
        project_id,
        session
    )
    if project.fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Закрытый проект нельзя редактировать!'
        )


async def check_full_amount(
        project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession,
) -> None:
    """Требуемая сумма больше или равна вложенной."""
    if obj_in.full_amount:
        project: CharityProject = await charity_project_crud.get(
            project_id,
            session)

        if project.invested_amount > obj_in.full_amount:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=(
                    'Нельзя установить требуемую сумму меньше уже вложенной!'
                )
            )
