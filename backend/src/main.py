from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()


@app.get("/dataset/abus/download")
def anos_download(token: str):
    print(f"token: {token}")
    return FileResponse("../data/abus.zip", filename="abus.zip",media_type="application/octet-stream")

@app.get("/")
def default():
    return JSONResponse(
        content={
            "application":"iipl", 
            "version":"1.0.0", 
            "email": "dev@iipl.ir",
            "documentation": "/docs",
        },
        status_code=200
        )