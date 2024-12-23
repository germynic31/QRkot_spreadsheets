from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_full_amount, check_invested_for_delete,
                                check_project_exists,
                                check_project_name_duplicate,
                                check_update_on_close_project)
from app.core.constants import PROJECTS_URL
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.project import charity_project_crud
from app.models import CharityProject
from app.schemas.project import (CharityProjectCreate, CharityProjectDB,
                                 CharityProjectUpdate)
from app.services.investment import invest


router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
    summary='Создает благотворительный проект.'
)
async def create_new_charity_project(
        charity_project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
) -> CharityProject:
    await check_project_name_duplicate(charity_project.name, session)
    new_project: CharityProject = await charity_project_crud.create(
        charity_project,
        session
    )
    await invest(project=new_project, session=session)
    return new_project


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    summary='Выводит список всех проектов'
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
) -> list[CharityProject]:
    return await charity_project_crud.get_multi(session)


@router.patch(
    PROJECTS_URL,
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
    summary='Обновляет проект.'
)
async def partially_update_charity_project(
        project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
) -> CharityProject:
    project = await check_project_exists(
        project_id, session
    )
    await check_project_name_duplicate(obj_in.name, session)
    await check_update_on_close_project(project_id, session)
    await check_full_amount(project_id, obj_in, session)
    project: CharityProject = await charity_project_crud.update(
        project, obj_in, session
    )
    await invest(project=project, session=session)
    return project


@router.delete(
    PROJECTS_URL,
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
    summary='Удаляет проект, но только если в него не было вложено денег.'
)
async def remove_charity_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),
) -> CharityProject:
    project: CharityProject = await check_project_exists(
        project_id, session
    )
    await check_invested_for_delete(
        project_id, session
    )
    return await charity_project_crud.remove(
        project, session
    )
