from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

from app.helpers import process_data

app = FastAPI()


@app.get("/")
async def root():
    return HTMLResponse(content=open("app/index.html", "r").read())


@app.post("/")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
