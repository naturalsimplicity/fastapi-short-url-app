from fastapi import APIRouter, Depends, Path, HTTPException
from fastapi.responses import RedirectResponse
from starlette import status
from typing import Annotated
from pydantic import HttpUrl

from shorturl.models.urls import Url, ShortUrl, ShortURLInfo
from shorturl.services.urls import UrlsService
from shorturl.dependencies.database import get_service
from shorturl.exceptions import FullURLNotFoundError
from shorturl.resources import strings

router = APIRouter(
    prefix="/urls",
    tags=['URLs']
)

@router.post("/shorten")
async def create_short_url(
    url: Url,
    urls_service: Annotated[UrlsService, Depends(get_service(UrlsService))]
) -> ShortUrl:
    return await urls_service.get_short_url(full_url=str(url.full_url))

@router.get("/stats/{short_id}")
async def get_full_url(
    short_id: Annotated[
        str,
        Path(
            title=ShortUrl.__pydantic_fields__['short_id'].title,
            examples=[1]
        )
    ],
    urls_service: Annotated[UrlsService, Depends(get_service(UrlsService))]
) -> ShortURLInfo:
    try:
        url = await urls_service.get_full_url(short_id=short_id)
        return ShortURLInfo(
            short_id=short_id,
            full_url=HttpUrl(url)
        )
    except FullURLNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.FULL_URL_NOT_FOUND
        )

@router.get("/{short_id}")
async def redirect_to_full_url(
    short_id: Annotated[
        str,
        Path(
            title=ShortUrl.__pydantic_fields__['short_id'].title,
            examples=[1]
        )
    ],
    urls_service: Annotated[UrlsService, Depends(get_service(UrlsService))]
):
    try:
        url = await urls_service.get_full_url(short_id=short_id)
        return RedirectResponse(url=url)
    except FullURLNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.FULL_URL_NOT_FOUND
        )