import os
import sys

import uvicorn
from fastapi import FastAPI ,status
import models
import registerBase

from db import init_db , database
from settings import cfg

version = f"{sys.version_info.major}.{sys.version_info.minor}"


app = FastAPI(
    title="Project FastAPI",
    description="ProjectFinal",
    version="1.0",
    root_path=os.getenv("ROOT_PATH", "")
)

if cfg.MODE == "dev":
    from fastapi.middleware.cors import CORSMiddleware
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI . Using Python {version}"
    return {"message": message}

app.include_router(
    registerBase.router,
    prefix="/info",
    tags=["Trainee_info_dev"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "info Not Found"}}
)



@app.on_event("startup")
async def startup():
    await  database.connect()
    init_db()


@app.on_event("shutdown")
async def shutdown():
    await  database.disconnect()


if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        workers=1,
        proxy_headers=True,
        forwarded_allow_ips="*",
        root_path=os.getenv("ROOT_PATH", ""),
    )
