import sys
import os

# اضافه کردن مسیر ریشه پروژه به sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from app.models.repayment_model import predict_action
import streamlit as st

st.set_page_config(page_title="Darj Smart Collection", page_icon="📊")

st.title("📊 Darj Smart Collection Dashboard")
st.markdown("این داشبورد به شما کمک می‌کند تا بر اساس ویژگی‌های مشتری، بهترین اقدام وصول را انتخاب کنید.")

# ورودی‌ها
delay_days = st.slider("تعداد روزهای تأخیر", 0, 180, 30)
contact_count = st.slider("تعداد تماس‌ها", 0, 10, 2)
promise_given = st.selectbox("آیا مشتری قول داده؟", ["بله", "خیر"]) == "بله"
promise_kept = st.selectbox("آیا مشتری به قولش عمل کرده؟", ["بله", "خیر"]) == "بله"

# پیش‌بینی
if st.button("پیشنهاد اقدام"):
    result = predict_action(
        delay_days=delay_days,
        contact_count=contact_count,
        promise_given=promise_given,
        promise_kept=promise_kept
    )
    st.success(f"✅ پیشنهاد سیستم: **{result}**")

# درباره پروژه
with st.expander("ℹ️ درباره پروژه"):
    st.markdown("""
    این پروژه با استفاده از FastAPI و مدل یادگیری ماشین طراحی شده تا به بانک‌ها در تصمیم‌گیری هوشمندانه برای وصول مطالبات کمک کند.
    """)