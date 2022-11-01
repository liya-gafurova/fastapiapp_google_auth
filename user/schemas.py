from typing import Optional

from pydantic import BaseModel, EmailStr


class GoogleUserSchema(BaseModel):
    username:str
    email: EmailStr
    avatar: str


class CreateFromGoogleUserSchema(GoogleUserSchema):
    google_token: str


class UserDB(BaseModel):
    id: str
    username: str
    email: Optional[str]


class TokenModel(BaseModel):
    token: str
    userid: str