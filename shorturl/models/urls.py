from pydantic import BaseModel, Field, HttpUrl


class Url(BaseModel):
    full_url: HttpUrl = Field(
        title='Full URL',
        min_length=1
    )

class ShortUrl(BaseModel):
    short_id: str = Field(
        title="Short ID of full URL"
    )

class ShortURLInfo(ShortUrl, Url):
    ...
