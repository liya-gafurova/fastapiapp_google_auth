import uuid
from typing import Optional, Union

from pydantic import BaseModel
from pydantic.schema import datetime

IdType = Union[str, int, uuid.UUID]


class PostDB(BaseModel):
    id: IdType
    title: Optional[str]
    text: str
    created: Optional[datetime]

    class Config:
        orm_mode=True


class PostCreate(BaseModel):
    title: Optional[str]
    text: str


class PostRead(PostDB):
    pass



