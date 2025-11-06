from app.db.models import Base
from app.db.database import engine

Base.metadata.create_all(bind=engine)
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
def welcome():
    return {"message": "Welcome to Darj Smart Collection API"}


# روت پیش‌بینی
@app.post("/predict")
def predict(data: InputData):
    result = predict_action(
        delay_days=data.delay_days,
        contact_count=data.contact_count,
        promise_given=data.promise_given,
        promise_kept=data.promise_kept
    )

    # ذخیره در دیتابیس
    from app.db.database import SessionLocal
    from app.db.models import RepaymentRecord

    db = SessionLocal()
    record = RepaymentRecord(
        delay_days=data.delay_days,
        contact_count=data.contact_count,
        promise_given=data.promise_given,
        promise_kept=data.promise_kept,
        recommended_action=result
    )
    db.add(record)
    db.commit()
    db.close()

    return {"recommended_action": result}