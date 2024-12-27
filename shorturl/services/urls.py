from aiosqlite import Connection, IntegrityError
import hashlib

from shorturl.services.base import BaseService
from shorturl.models.urls import ShortUrl, Url
from shorturl.database.queries import queries
from shorturl.exceptions import FullURLNotFoundError


class UrlsService(BaseService):
    def __init__(self, conn: Connection) -> None:
        super().__init__(conn)

    @staticmethod
    def _generate_short_id(full_url: str, length: int = 8) -> str:
        url_bytes = full_url.encode('utf-8')
        hash_object = hashlib.md5(url_bytes)
        hash_hex_string = hash_object.hexdigest()
        return hash_hex_string[:length]

    async def get_short_url(
        self,
        full_url: str
    ) -> ShortUrl:
        short_id = await queries.get_short_id(
            self.connection,
            full_url=full_url
        )
        if not short_id:
            short_id = self._generate_short_id(full_url)
            print(short_id)
            await queries.create_new_url(
                self.connection,
                short_id=short_id,
                full_url=full_url
            )
            await self.connection.commit()
        return ShortUrl(short_id=short_id)

    async def get_full_url(
        self,
        short_id: str
    ) -> str:
        full_url = await queries.get_full_url(
            self.connection,
            short_id=short_id
        )
        if not full_url:
            raise FullURLNotFoundError
        return full_url
