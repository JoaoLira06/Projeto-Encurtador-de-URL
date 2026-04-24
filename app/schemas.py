from pydantic import BaseModel, HttpUrl
from datetime import datetime

class URLCreate(BaseModel):
    original_url: HttpUrl

class URLResponse(BaseModel):
    short_code:str
    original_url: str
    short_url: str

    class Config:
        from_attributes = True
class URLStatus(BaseModel):
    short_code: str
    original_url: str
    access_count: int
    created_at: datetime
