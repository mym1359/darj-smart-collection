import pandas as pd
import xgboost as xgb
import os

# آموزش مدل با داده‌های فرضی
def train_model():
    data = pd.DataFrame({
        "delay_days": [10, 45, 90, 120, 5, 60],
        "contact_count": [1, 3, 5, 2, 0, 4],
        "promise_given": [1, 1, 0, 1, 0, 1],
        "promise_kept": [0, 0, 0, 1, 0, 1],
        "action": [2, 0, 1, 3, 1, 3]  # 0=Call, 1=SMS, 2=Legal, 3=Wait
    })

    X = data.drop("action", axis=1)
    y = data["action"]

    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric="mlogloss")
    model.fit(X, y)

    # ذخیره مدل
    model.save_model("app/models/xgb_model.json")

# پیش‌بینی با مدل آموزش‌دیده
def predict_action_ml(delay_days, contact_count, promise_given, promise_kept):
    model_path = "app/models/xgb_model.json"
    if not os.path.exists(model_path):
        train_model()

    model = xgb.XGBClassifier()
    model.load_model(model_path)

    input_df = pd.DataFrame([{
        "delay_days": delay_days,
        "contact_count": contact_count,
        "promise_given": int(promise_given),
        "promise_kept": int(promise_kept)
    }])

    prediction = model.predict(input_df)[0]
    actions = ["Call", "SMS", "Legal", "Wait"]
    return actions[prediction]