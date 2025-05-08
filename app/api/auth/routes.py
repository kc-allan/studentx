from fastapi import APIRouter, Depends, HTTPException, FastAPI

auth = APIRouter(prefix="/auth", tags=["auth"])


@auth.get('/login', response_model=dict, status_code=200)
def login():
    """
    Index route.
    """
    return {"message": "Hello world!"}
