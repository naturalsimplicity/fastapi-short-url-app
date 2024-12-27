from typing import Annotated, AsyncGenerator, Callable, Type, Any
from aiosqlite import Connection, connect
from fastapi import Depends

from shorturl.core.settings import settings
from shorturl.services.base import BaseService


async def _get_connection() -> AsyncGenerator[Connection, Any]:
    async with connect(f"{settings.database_path}") as conn:
        yield conn

def get_service(
    service_type: Type[BaseService],
) -> Callable[[Connection], BaseService]:
    def _get_service(
        conn: Annotated[Connection, Depends(_get_connection)],
    ) -> BaseService:
        return service_type(conn)

    return _get_service
