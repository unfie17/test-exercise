import csv
from time import sleep

from fastapi import FastAPI, Body, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI()

with open('binlist-data.csv', 'r') as file:
    bin_db = {info['bin']: info for info in csv.DictReader(file)}


@app.get("/ping")
async def ping():
    return 'pong'


@app.post("/get-info")
async def get_info(data=Body()):
    if not data:
        raise HTTPException(status_code=400, detail="Empty request body")

    if data.get('bin_number') is None:
        raise HTTPException(status_code=400, detail="No 'bin_number' field in request")
    raw_bin_number = data["bin_number"]

    if not isinstance(raw_bin_number, str):
        raise HTTPException(status_code=400, detail="BIN number should be string")
    bin_number = raw_bin_number.strip()

    if not raw_bin_number:
        raise HTTPException(status_code=400, detail="BIN number can't be empty")
    try:
        float(bin_number)
    except ValueError:
        raise HTTPException(status_code=400, detail="BIN number should contain only digits")

    if len(bin_number) < 6:
        raise HTTPException(status_code=400, detail="BIN number's length can't be less than 6")

    if len(bin_number) > 8:
        raise HTTPException(status_code=400, detail="BIN number's length can't be greater than 8")

    sleep(3)
    if bin_number not in bin_db.keys():
        raise HTTPException(status_code=404, detail="Unknown BIN")
    return {"data": bin_db[bin_number]}


app.mount("/", StaticFiles(directory="html", html=True))
