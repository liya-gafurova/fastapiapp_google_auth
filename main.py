import uvicorn
from fastapi import FastAPI

from db.db import engine, Base
from routers import router
from user.routers import auth_router

app = FastAPI()

app.include_router(router, prefix='/posts', tags=['Posts'])
app.include_router(auth_router,)

@app.on_event('startup')
async def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8084, log_level='info')