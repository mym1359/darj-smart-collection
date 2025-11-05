from fastapi import FastAPI
from app.routes.actions import router

app = FastAPI(
    title="Darj Smart Collection API",
    description="هوشمندسازی وصول مطالبات بانکی با تحلیل رفتار مشتری و پیشنهاد مسیر بهینه",
    version="1.0.0"
)

app.include_router(router)