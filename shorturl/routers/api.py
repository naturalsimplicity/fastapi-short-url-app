from fastapi import APIRouter

from shorturl.routers.v1 import urls


router = APIRouter(
    prefix='/v1'
)

router.include_router(urls.router)
