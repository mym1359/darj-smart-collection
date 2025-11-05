from fastapi import APIRouter
from pydantic import BaseModel
from app.models.repayment_model import train_model
from app.services.recommender import recommend_action

router = APIRouter()

class CustomerFeatures(BaseModel):
    delay_days: int
    contact_count: int
    promise_given: bool
    promise_kept: bool

@router.get("/")
def welcome():
    return {"message": "Welcome to Darj Smart Collection API"}

@router.post("/recommend")
def get_recommendation(features: CustomerFeatures):
    action = recommend_action(features.model_dump())
    return {"recommended_action": action}

@router.get("/train-model")
def train():
    train_model()
    return {"message": "Model trained and saved successfully"}