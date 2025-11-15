from fastapi import FastAPI
from pydantic import BaseModel
from app.db.models import Base, RepaymentRecord
from app.db.database import engine, SessionLocal
from app.models.repayment_model import predict_action
from app.models.ml_model import predict_action_ml

# ساخت جداول دیتابیس
Base.metadata.create_all(bind=engine)

# تعریف اپلیکیشن FastAPI
app = FastAPI()

# مدل ورودی
class InputData(BaseModel):
    delay_days: int
    contact_count: int
    promise_given: bool
    promise_kept: bool

# روت خوش‌آمدگویی
@app.get("/")
def welcome():
    return {"message": "Welcome to Darj Smart Collection API"}

# روت پیش‌بینی کلاسیک
@app.post("/predict")
def predict(data: InputData):
    result = predict_action(
        delay_days=data.delay_days,
        contact_count=data.contact_count,
        promise_given=data.promise_given,
        promise_kept=data.promise_kept
    )

    # محاسبه outcome (موفقیت)
    outcome = data.promise_given and data.promise_kept

    # ذخیره در دیتابیس
    db = SessionLocal()
    record = RepaymentRecord(
        delay_days=data.delay_days,
        contact_count=data.contact_count,
        promise_given=data.promise_given,
        promise_kept=data.promise_kept,
        recommended_action=result,
        outcome=outcome
    )
    db.add(record)
    db.commit()
    db.close()

    return {"recommended_action": result}

# روت پیش‌بینی با مدل ML
@app.post("/predict_ml")
def predict_ml(data: InputData):
    action = predict_action_ml(
        delay_days=data.delay_days,
        contact_count=data.contact_count,
        promise_given=data.promise_given,
        promise_kept=data.promise_kept
    )
    return {"recommended_action": action}