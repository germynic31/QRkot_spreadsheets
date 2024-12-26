from copy import deepcopy
from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import settings
from app.core.constants import (COLUMN_COUNT, FORMAT, ROW_COUNT,
                                VALUE_INPUT_OPTION)


SPREADSHEET_BODY_SAMPLE = dict(
    properties=dict(
        title='Отчёт',
        locale='ru_RU'
    ),
    sheets=[dict(properties=dict(
        sheetType='GRID',
        sheetId=0,
        title='Лист1',
        gridProperties=dict(
            rowCount=ROW_COUNT,
            columnCount=COLUMN_COUNT
        )
    ))]
)

TABLE_HEADER_SAMPLE = [
    ['Отчёт от'],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]


async def spreadsheets_create(wrapper_services: Aiogoogle) -> tuple[str, str]:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = deepcopy(SPREADSHEET_BODY_SAMPLE)
    spreadsheet_body['properties']['title'] = f'Отчёт на {now_date_time}'
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    return response['spreadsheetId'], response['spreadsheetUrl']


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields='id'
        )
    )


async def spreadsheets_update_value(
        spreadsheetid: str,
        projects: list,
        wrapper_services: Aiogoogle
) -> None:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')

    table_header = deepcopy(TABLE_HEADER_SAMPLE)
    table_header[0].append(now_date_time)
    table_values = [
        *table_header,
        *[list(map(str, project)) for project in projects]
    ]

    len_add_rows = len(projects) + len(TABLE_HEADER_SAMPLE)
    if ROW_COUNT <= len_add_rows:
        raise MemoryError(
            f'Недостаточно строк в таблице для записи '
            f'(count rows:{ROW_COUNT} <= count projects:{len_add_rows})'
        )

    len_add_columns = len(TABLE_HEADER_SAMPLE[2])
    if COLUMN_COUNT <= len_add_columns:
        raise MemoryError(
            f'Недостаточно колонок в таблице для записи '
            f'(count columns:{COLUMN_COUNT} <= count fields:{len_add_columns})'
        )

    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range=f'R1C1:R{len_add_rows}C{len_add_columns}',
            valueInputOption=VALUE_INPUT_OPTION,
            json={
                'majorDimension': 'ROWS',
                'values': table_values
            }
        )
    )
