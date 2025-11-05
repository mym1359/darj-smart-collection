# Darj Smart Collection System

هوشمندسازی فرآیند وصول مطالبات بانکی با تحلیل رفتار مشتری و پیشنهاد مسیر بهینه وصول با استفاده از هوش مصنوعی

---

## 🧠 Project Overview

Darj Smart Collection is an AI-powered debt recovery system designed for banking environments. It analyzes customer repayment behavior and recommends optimal collection strategies to maximize efficiency and minimize delays.

This project is based on real-world experience from Maskan Bank (Iran) and demonstrates scalable, secure, and intelligent automation aligned with global fintech standards.

---

## 🚀 Key Features

- **Behavioral Analysis**: Predicts repayment likelihood using machine learning models
- **Smart Recommendations**: Suggests optimal actions (call, warning, legal) based on customer profile
- **Automated Reminders**: Tracks promises and triggers follow-ups
- **Action Logging**: Records all user interactions for audit and performance tracking
- **Branch & User Dashboards**: Visualizes collection performance and KPIs
- **Letter Generation**: Automates official warnings and legal notices

---

## 🛠️ Technologies Used

| Layer       | Tools & Libraries |
|-------------|-------------------|
| Backend     | Python, FastAPI   |
| AI/ML       | Scikit-learn, XGBoost, PyCaret |
| NLP         | spaCy, Transformers |
| Frontend    | React (planned)   |
| Database    | PostgreSQL        |
| Automation  | Celery, Redis     |
| DevOps      | GitHub Actions    |
| Security    | OAuth2, JWT       |

---

## 📦 Installation

```bash
git clone https://github.com/mym1359/darj-smart-collection.git
cd darj-smart-collection
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

🧪 Run Model Training
python app/models/repayment_model.py

📊 Run API Server (FastAPI)
uvicorn app.main:app --reload

🌍 Migration Impact
This project showcases advanced AI-based debt collection strategies tailored for banking systems. It reflects real-world experience in Iran's banking sector and demonstrates scalable, secure, and intelligent automation aligned with U.S. financial technology standards.
It is designed to support professional recognition and migration goals by highlighting:
• 	Technical excellence in Python and AI
• 	Real-world banking impact
• 	Scalable architecture and automation
• 	Bilingual documentation and global relevance

📈 Roadmap
• 	[x] Initial model training
• 	[x] Action recommender system
• 	[ ] FastAPI endpoints for user actions
• 	[ ] Frontend dashboard with React
• 	[ ] NLP-based promise tracking
• 	[ ] Deployment on cloud (Docker + CI/CD)

🤝 Contact
Developed by Mohammad Yadollah Moghadam
Banking Expert & Web Developer at Maskan Bank
Specialized in AI-driven financial solution