from pydantic import BaseModel

class PredictionRequest(BaseModel):
    total_sqft: float
    location: str
    bhk:int
    bath: int
    
