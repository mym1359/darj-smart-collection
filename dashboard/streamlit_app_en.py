import streamlit as st
st.set_page_config(page_title="Darj Smart Collection - Analytics", layout="wide")

import requests
import sys
import os
import pandas as pd
import sqlite3
import altair as alt
import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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

# 📅 Filter by date
st.sidebar.header("📅 Filter by date")
days = st.sidebar.slider("Show records from last N days", 1, 180, 30)
cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)

# 📊 Recommended Action Distribution
st.title("📊 Recommended Action Distribution")

# اتصال به دیتابیس
conn = sqlite3.connect("repayment.db")
query = "SELECT recommended_action FROM repayment_records"
df = pd.read_sql(query, conn)

if df.empty:
    st.warning("No data available yet. Submit predictions via the API to populate the dashboard.")
else:
    # شمارش اقدامات
    action_counts = df["recommended_action"].value_counts().reset_index()
    action_counts.columns = ["Action", "Count"]

    # نمودار ستونی
    chart = alt.Chart(action_counts).mark_bar().encode(
        x=alt.X("Action", sort="-y"),
        y="Count",
        color="Action",
        tooltip=["Action", "Count"]
    ).properties(
        width=600,
        height=400,
        title=f"Distribution of Recommended Actions (Last {days} Days)"
    )

    st.altair_chart(chart, use_container_width=True)
    
# 📈 Success Rate by Action
st.subheader("📈 Success Rate by Action")

query_success = """
SELECT recommended_action, COUNT(*) as total,
SUM(CASE WHEN outcome = 1 THEN 1 ELSE 0 END) as success
FROM repayment_records
GROUP BY recommended_action
"""
df_success = pd.read_sql(query_success, conn)

if df_success.empty:
    st.info("No success data available yet.")
else:
    df_success["Success Rate (%)"] = (df_success["success"] / df_success["total"] * 100).round(1)

    chart_success = alt.Chart(df_success).mark_bar().encode(
        x=alt.X("recommended_action", title="Action"),
        y=alt.Y("Success Rate (%)"),
        color="recommended_action",
        tooltip=["recommended_action", "Success Rate (%)", "total", "success"]
    ).properties(
        width=600,
        height=400,
        title="Success Rate by Recommended Action"
    )

    st.altair_chart(chart_success, use_container_width=True)
    
