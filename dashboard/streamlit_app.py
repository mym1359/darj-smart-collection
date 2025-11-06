import streamlit as st
import requests
import sys
import os

# اضافه کردن مسیر پروژه برای اطمینان از دسترسی به فایل‌ها (در صورت نیاز به import مستقیم)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# تنظیمات صفحه
st.set_page_config(page_title="Darj Smart Collection", page_icon="📊")

st.title("📊 Darj Smart Collection Dashboard")
st.markdown("این داشبورد به شما کمک می‌کند تا بر اساس ویژگی‌های مشتری، بهترین اقدام وصول را انتخاب کنید.")

# ورودی‌ها
delay_days = st.slider("تعداد روزهای تأخیر", 0, 180, 30)
contact_count = st.slider("تعداد تماس‌ها", 0, 10, 2)
promise_given = st.selectbox("آیا مشتری قول داده؟", ["بله", "خیر"]) == "بله"
promise_kept = st.selectbox("آیا مشتری به قولش عمل کرده؟", ["بله", "خیر"]) == "بله"

# تابع اتصال به API
def predict_action_api(delay_days, contact_count, promise_given, promise_kept):
    url = "http://localhost:8000/predict"
    payload = {
        "delay_days": delay_days,
        "contact_count": contact_count,
        "promise_given": promise_given,
        "promise_kept": promise_kept
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["recommended_action"]
    except requests.exceptions.RequestException as e:
        return f"❌ خطا در اتصال به API: {e}"

# دکمه پیش‌بینی
if st.button("پیشنهاد اقدام"):
    result = predict_action_api(
        delay_days=delay_days,
        contact_count=contact_count,
        promise_given=promise_given,
        promise_kept=promise_kept
    )
    st.success(f"✅ پیشنهاد سیستم: **{result}**")

# درباره پروژه
with st.expander("ℹ️ درباره پروژه"):
    st.markdown("""
    این پروژه با استفاده از FastAPI و Streamlit طراحی شده تا به بانک‌ها در تصمیم‌گیری هوشمندانه برای وصول مطالبات کمک کند.
    """)


from app.db.database import SessionLocal
from app.db.models import RepaymentRecord

def load_records():
    db = SessionLocal()
    records = db.query(RepaymentRecord).order_by(RepaymentRecord.id.desc()).all()
    db.close()
    return records

with st.expander("📋 نمایش سوابق ثبت‌شده"):
    records = load_records()
    if records:
        st.write("آخرین اقدامات ثبت‌شده:")
        data = [
            {
                "تأخیر (روز)": r.delay_days,
                "تعداد تماس": r.contact_count,
                "قول داده؟": "بله" if r.promise_given else "خیر",
                "قول را عمل کرده؟": "بله" if r.promise_kept else "خیر",
                "پیشنهاد سیستم": r.recommended_action
            }
            for r in records
        ]
        st.table(data)
    else:
        st.info("هنوز هیچ رکوردی ثبت نشده است.")