from fastapi import HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class Settings(BaseModel):
    auth_jwt_secret: str = 'ca8fe4b432ad619947191b84037496b7086d5518c2968ef9a745b6575d69ddfd'


@AuthJWT.load_config
def load_config(settings: Settings):
    return Settings.auth_jwt_secret
