import datetime
from pydantic import BaseModel


class BasePublik(BaseModel):
    title: str
    description: str
    reader: str
    admin: str
    moderator: str

class Publik(BasePublik):
    id: int
    user_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


class PublikIn(BasePublik):
    pass