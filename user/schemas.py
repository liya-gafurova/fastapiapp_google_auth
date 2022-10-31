from pydantic import BaseModel, EmailStr


class GoogleUserSchema(BaseModel):
    username:str
    email: EmailStr
    avatar: str


class CreateFromGoogleUserSchema(GoogleUserSchema):
    google_token: str