from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from deps import get_db
from repository.posts import crud_post
from schemas import PostRead, IdType, PostCreate, PostDB
from utils import generate_uuid

router = APIRouter()


@router.get('', response_model=List[PostRead])
async def get_posts(db=Depends(get_db)):
    posts = crud_post.get_multi(db=db)

    return posts


@router.get('/{id}', response_model=PostRead)
async def get_post(id: IdType, db= Depends(get_db)):
    post = crud_post.get(db=db, id=id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return post


@router.post('/create', response_model=PostRead)
async def create_post(post: PostCreate, db = Depends(get_db)):

    post: PostDB = PostDB(
        id = generate_uuid(),
        **post.dict()
    )

    db_obj = crud_post.create(db=db, obj_in=post)

    return db_obj