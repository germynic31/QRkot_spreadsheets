import logging

from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.exceptions import NotEnoughSpaceInTable
from app.core.google_client import get_service
from app.core.user import current_superuser
from app.crud.project import charity_project_crud
from app.services.google_api import (set_user_permissions, spreadsheets_create,
                                     spreadsheets_update_value)


router = APIRouter()


@router.get(
    '/',
    dependencies=[Depends(current_superuser)],
    summary='Создает таблицу с топом проектов по скорости закрытия.'
)
async def get_top(
        session: AsyncSession = Depends(get_async_session),
        wrapper_services: Aiogoogle = Depends(get_service)

):
    projects = await charity_project_crud.get_projects_by_completion_rate(
        session
    )
    spreadsheet_id, spreadsheet_url = await spreadsheets_create(
        wrapper_services
    )
    await set_user_permissions(spreadsheet_id, wrapper_services)
    try:
        await spreadsheets_update_value(
            spreadsheet_id,
            projects,
            wrapper_services
        )
    except NotEnoughSpaceInTable:
        error_message = 'Недостаточно места в таблице для записи'
        logging.error(error_message)
        raise HTTPException(
            status_code=400,
            detail=error_message
        )
    except Exception as e:
        error_message = f'Произошла непредвиденная ошибка: {e}'
        logging.error(error_message)
        raise HTTPException(
            status_code=500,
            detail=error_message
        )
    return spreadsheet_url
