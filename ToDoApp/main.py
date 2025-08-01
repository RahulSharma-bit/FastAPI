from fastapi import FastAPI
import models
from Database import engine
from routers import auth, todos, admin, users

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get("/healthy")
def health_check():
    return {'status' : 'Healthy'}

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)

