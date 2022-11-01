from fastapi import APIRouter, Depends
from starlette import status
from starlette.requests import Request
from starlette.responses import Response
from starlette.templating import Jinja2Templates

from fastapi import HTTPException

from deps import get_db
from repository.users import crud_users
from utils import generate_uuid
from . import tokenizator
from google.oauth2 import id_token
from google.auth.transport import requests

from user.schemas import *

auth_router = APIRouter()
GOOGLE_CLIENT_ID = "611022650187-bku2b5piqeflrmreknl8to8omklnj46g.apps.googleusercontent.com"

# http://127.0.0.1:4000/auth/google
templates = Jinja2Templates(directory="templates")


@auth_router.get('/')
async def get_html(request: Request):
    return templates.TemplateResponse("auth2.html", {"request": request})


async def create_user(db, user: CreateFromGoogleUserSchema):
    user_db = crud_users.create(db=db, obj_in=UserDB(id=generate_uuid(),
                                                     username=user.username,
                                                     email=user.email))

    return user_db


async def google_auth(db, user) -> tuple:
    try:
        idinfo = id_token.verify_oauth2_token(user.google_token, requests.Request(), GOOGLE_CLIENT_ID)
    except ValueError:
        raise HTTPException(403, "Bad code")
    user = await create_user(db, user)
    internal_token = tokenizator.create_token(user.id)
    return user.id, internal_token.get("access_token")


@auth_router.post('/auth/google')
async def login_google(create_user: CreateFromGoogleUserSchema, db=Depends(get_db)):
    userid, token = await google_auth(db, create_user)
    return TokenModel(token=token, userid=userid)
