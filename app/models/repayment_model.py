import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_loans.csv')
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'repayment_model.pkl')


def load_data(path=DATA_PATH):
    df = pd.read_csv(path)
    df['promise_given'] = df['promise_given'].map({'yes': 1, 'no': 0})
    df['promise_kept'] = df['promise_kept'].map({'yes': 1, 'no': 0})
    df.fillna(0, inplace=True)
    return df


def train_model():
    df = load_data()
    features = ['delay_days', 'contact_count', 'promise_given']
    target = 'promise_kept'

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("📊 Classification Report:")
    print(classification_report(y_test, y_pred))
    print("🧩 Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    joblib.dump(model, MODEL_PATH)
    print(f"✅ Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    train_model()