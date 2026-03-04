from fastapi import  FastAPI
import models
from db import engine


from routes import auth
from routes import todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)





app.include_router(auth.router)
app.include_router(todos.router)