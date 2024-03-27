from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from . import util

app = FastAPI()

class PredictionRequest(BaseModel):
    total_sqft: float
    location: str
    bhk: int
    bath: int

@app.on_event("startup")
async def startup_event():
    util.load_saved_artifacts()

@app.get('/get_location_names')
async def get_location_names():
    locations = util.get_location_names()
    return JSONResponse(content={'locations': locations}, headers={'Access-Control-Allow-Origin': '*'})

@app.post('/predict_home_price')
async def predict_home_price(request_data: PredictionRequest):
    try:
        estimated_price = util.get_estimated_price(
            request_data.location,
            request_data.total_sqft,
            request_data.bhk,
            request_data.bath
        )
        return {'estimated_price': estimated_price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
