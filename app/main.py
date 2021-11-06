from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.helpers import get_predictions, process_data

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
async def root():
    return HTMLResponse(content=open("app/static/app.html", "r").read())


@app.post("/")
async def upload_file(file: UploadFile = File(...)):
    x = process_data(file.file)
    return get_predictions(x)
