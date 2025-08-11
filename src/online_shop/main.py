import uvicorn
from fastapi import FastAPI

from online_shop.resources import router


def get_app():
    app = FastAPI()
    app.include_router(router)
    return app


app = get_app()

uvicorn.run(app, host="0.0.0.0", port=8000)
