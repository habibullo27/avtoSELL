from fastapi import FastAPI
from api.photo.photo_api import photo_router
from api.users.user_api import users_router
from database import engine,Base
app = FastAPI(docs_url="/")
Base.metadata.create_all(bind=engine)
app.include_router(users_router)
app.include_router(photo_router)

# uvicorn main:app --reload
