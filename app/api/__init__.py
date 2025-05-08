from fastapi import FastAPI
from app.api.auth.routes import auth as auth_router

apiApp = FastAPI()
@apiApp.get("/")
def root():
    return {"message": "FastAPI is live"}
apiApp.include_router(auth_router)