import streamlit as st
import requests
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

st.set_page_config(page_title="Darj Smart Collection", page_icon="📊")

st.title("📊 Darj Smart Collection Dashboard")
st.markdown("This dashboard helps you choose the best debt collection action based on customer behavior.")

# Inputs
delay_days = st.slider("Delay in days", 0, 180, 30)
contact_count = st.slider("Number of contacts", 0, 10, 2)
promise_given = st.selectbox("Has the customer promised to pay?", ["Yes", "No"]) == "Yes"
promise_kept = st.selectbox("Has the customer kept the promise?", ["Yes", "No"]) == "Yes"

# API call
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
        return f"❌ API connection error: {e}"

# Predict button
if st.button("Get Recommendation"):
    result = predict_action_api(
        delay_days=delay_days,
        contact_count=contact_count,
        promise_given=promise_given,
        promise_kept=promise_kept
    )
    st.success(f"✅ Recommended action: **{result}**")

# Show stored records
from app.db.database import SessionLocal
from app.db.models import RepaymentRecord

def load_records():
    db = SessionLocal()
    records = db.query(RepaymentRecord).order_by(RepaymentRecord.id.desc()).all()
    db.close()
    return records

with st.expander("📋 View stored records"):
    records = load_records()
    if records:
        st.write("Latest prediction history:")
        data = [
            {
                "Delay (days)": r.delay_days,
                "Contacts": r.contact_count,
                "Promised?": "Yes" if r.promise_given else "No",
                "Kept promise?": "Yes" if r.promise_kept else "No",
                "Recommended action": r.recommended_action
            }
            for r in records
        ]
        st.table(data)
    else:
        st.info("No records found yet.")

# About
with st.expander("ℹ️ About this project"):
    st.markdown("""
    This project uses FastAPI and Streamlit to support smart decision-making in banking debt collection.
    It is modular, scalable, and ready for production deployment.
    """)