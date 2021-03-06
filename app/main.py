import json
import pickle

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.helpers import get_predictions, process_data

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
model = pickle.load(open("model.pkl", "rb"))


@app.get("/")
async def root():
    return HTMLResponse(content=open("app/static/app.html", "r").read())


@app.post("/")
async def upload_file(data_file: UploadFile = File(...)):
    data = process_data(data_file.file)
    preds = get_predictions(data, model)
    data["Outcome"] = preds
    data.to_csv("outcome_data.csv")
    return json.dumps(data.to_dict("index"))
