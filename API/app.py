from fastapi import FastAPI
from routes import itens_routes

api = FastAPI()

api.include_router(itens_routes, prefix="/itens")


@api.get("/")
def read_root():
    return {"Hello": "World"}


@api.get("/about")
def read_about():
    return {"About": "This is a test for future projects"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api, host="localhost", port=8000)
