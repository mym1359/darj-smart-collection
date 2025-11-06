from fastapi import FastAPI
from pydantic import BaseModel
from app.models.repayment_model import predict_action

# تعریف اپلیکیشن FastAPI
app = FastAPI()

# مدل ورودی
class InputData(BaseModel):
    delay_days: int
    contact_count: int
    promise_given: bool
    promise_kept: bool

# روت خوش‌آمدگویی (اختیاری)
@app.get("/")
def read_root():
    return {"message": "Darj Smart Collection API is running"}

# روت پیش‌بینی
@app.post("/predict")
def predict(data: InputData):
    result = predict_action(
        delay_days=data.delay_days,
        contact_count=data.contact_count,
        promise_given=data.promise_given,
        promise_kept=data.promise_kept
    )
    return {"recommended_action": result}