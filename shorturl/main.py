from fastapi import FastAPI

from shorturl.core.settings import settings
from shorturl.routers.api import router


def get_application() -> FastAPI:
    application = FastAPI(**settings.fastapi_kwargs)
    application.include_router(router, prefix=settings.api_prefix)
    return application


app = get_application()
