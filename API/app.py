from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from routes import itens_routes
from auth import User, Settings

api = FastAPI()

api.include_router(itens_routes, prefix="/itens")


@api.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


@api.post('/login')
def login(user: User, authorize: AuthJWT = Depends()):
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=401, detail="Bad username or password")

    access_token = authorize.create_access_token(subject=user.username)
    return {"access_token": access_token}


@api.get('/user')
def user(authorize: AuthJWT = Depends()):
    authorize.jwt_required()

    current_user = authorize.get_jwt_subject()
    return {"user": current_user}


@api.get("/")
def read_root():
    return {"Hello": "World"}


@api.get("/about")
def read_about():
    return {"About": "This is a test for future projects"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("API.app:api", host="localhost", port=8000, reload=True)
