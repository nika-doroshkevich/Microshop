import uvicorn
from fastapi import FastAPI

from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


@app.get("/")
def hello_index():
    return {
        "message": "Hello index",
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
