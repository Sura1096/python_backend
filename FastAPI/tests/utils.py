from collections.abc import Sequence
from datetime import date
from typing import Any

from pydantic import BaseModel
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase


async def save_object(
    session: AsyncSession,
    model: type[DeclarativeBase],
    data: dict[str, Any],
    commit: bool = False,
) -> None:
    await session.execute(insert(model).values(**data))

    if commit:
        await session.commit()
    else:
        await session.flush()


def compare_dicts_and_db_models(
    result: Sequence[DeclarativeBase] | None,
    expected_result: Sequence[dict] | None,
    schema: type[BaseModel],
) -> bool:
    if result is None or expected_result is None:
        return result == expected_result

    for res_item, exp_item in zip(result, expected_result, strict=False):
        exp_item['id'] = res_item.id

    result_to_schema = [schema(**item.__dict__) for item in result]
    expected_result_to_schema = [schema(**item) for item in expected_result]

    equality_len = len(result_to_schema) == len(expected_result_to_schema)
    equality_obj = all(obj in expected_result_to_schema for obj in result_to_schema)
    return all((equality_len, equality_obj))


def check_response_get_last_trading_dates(
    result: list[dict] | None,
    expected_result: list[dict] | None,
) -> bool:
    if result is None or expected_result is None:
        return result == expected_result

    result[0]['date'] = date.fromisoformat(result[0]['date'])

    equality_len = len(result) == len(expected_result)
    equality_obj = result[0]['date'] == expected_result[0]['date']
    return all((equality_len, equality_obj))


def check_response_get_dynamics(
    result: list[dict] | None,
    expected_result: list[dict] | None,
    schema: type[BaseModel],
) -> bool:
    if result is None or expected_result is None:
        return result == expected_result

    for res_item, exp_item in zip(result, expected_result, strict=False):
        exp_item['id'] = res_item['id']
        res_item['date'] = date.fromisoformat(res_item['date'])
        res_item['created_on'] = date.fromisoformat(res_item['created_on'])
        res_item['updated_on'] = date.fromisoformat(res_item['updated_on'])

    result_to_schema = [schema(**item) for item in result]
    expected_result_to_schema = [schema(**item) for item in expected_result]

    equality_len = len(result_to_schema) == len(expected_result_to_schema)
    equality_obj = all(obj in expected_result_to_schema for obj in result_to_schema)
    return all((equality_len, equality_obj))
