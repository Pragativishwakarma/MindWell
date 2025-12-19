🧠 AI-Based Stress Level Prediction System:

An intelligent web-based application built using **Django and Machine Learning** to predict user stress levels based on **questionnaire responses, physiological parameters, and behavioral data**.
The system promotes early stress detection and mental wellness through real-time predictions, dashboards, and wellness tools.


📌 Project Overview:

Stress has become a major concern in modern lifestyles. This project uses **Machine Learning models** integrated with a **Django web application** to classify stress levels into:

* 🟢 Low Stress
* 🟡 Medium Stress
* 🔴 High Stress

The system provides:

* ML-based stress prediction
* Questionnaire-based assessment
* Mood tracking & journaling
* Task management
* Wellness resources
* Admin monitoring dashboard

---

## 🎯 Objectives

* Predict human stress levels using AI & ML
* Provide real-time stress analysis
* Promote mental health awareness
* Offer user-friendly wellness tools
* Enable scalable, data-driven stress monitoring

---

## 🛠️ Tech Stack

🔹 Backend:

* **Python 3.12**
* **Django 5.2**
* Scikit-learn
* NumPy, Pandas
* SQLite3

🔹 Frontend:

* HTML5, CSS3, JavaScript
* Bootstrap 5
* Chart.js
* AOS Animations

🔹 Machine Learning:

* Random Forest Classifier
* Logistic Regression (optional)
* Pickle (`.pkl`) model serialization

---

## 📂 Project Structure

 
AI-Stress-Level-Prediction-System/
│
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   ├── favicon.ico
│   │   └── assets/
│   │       ├── images/
│   │       └── css/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── Footer.jsx
│   │   │   └── Loader.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── AssessmentForm.jsx
│   │   │   └── ResultPage.jsx
│   │   │
│   │   ├── styles/
│   │   │   └── main.css
│   │   │
│   │   ├── App.js
│   │   └── index.js
│   │
│   └── package.json
│
├── backend/
│   ├── routes/
│   │   ├── authRoutes.js
│   │   ├── userRoutes.js
│   │   ├── stressPredictionRoutes.js​22
│   │   └── adminRoutes.js​
│   │
│   ├── controllers/
│   │   ├── authController.js
│   │   ├── predictionController.js
│   │   ├── adminController.js
│   │   └── userController.js
│   │
│   ├── models/
│   │   ├── UserModel.js
│   │   ├── AssessmentModel.js
│   │   └── DatasetModel.js
│   │
│   ├── middleware/
│   │   ├── authMiddleware.js
│   │   └── errorHandler.js
│   │
│   ├── config/
│   │   ├── dbConfig.js
│   │   └── envConfig.js
│   │
│   ├── utils/
│   │   ├── tokenHelper.js
│   │   └── dataPreprocessor.js
│   │
│   ├── app.js
│   └── server.js
│
├── ml-model/
│   ├── dataset/
│   │   └── stress_data.csv
│   │
│   ├── preprocessing/
│   │   └── preprocess.py
│   │
│   ├── models/
│   │   ├── trained_model.pkl
│   │   └── model_training.ipynb
│   │
│   ├── prediction/
│       └── predict.py
│
├── database/
│   ├── schema.sql​23
│   └── backup/​
│
├── documentation/
│   ├── Project_Report.docx
│   ├── Diagrams/
│   │   ├── DFD.png
│   │   ├── UseCase.png
│   │   └── Architecture.png
│   └── References.txt
│
├── .env
├── README.md
 
 
 

## ⚙️ Installation & Setup:

1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Stress-Level-Prediction-System.git
cd AI-Stress-Level-Prediction-System
```

2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

6️⃣ Run Server
```bash
python manage.py runserver
```

Open browser:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

# 🤖 Machine Learning Model:

* Dataset: Physiological & questionnaire-based data
* Algorithm: **Random Forest Classifier**
* Confidence scores provided for each prediction
* Model stored as `.pkl` and loaded dynamically in Django

---

# 👤 User Features:

* User Registration & Login
* Stress Questionnaire
* ML-based Stress Prediction
* Mood Tracking (1–10 scale)
* Task Manager
* Journal (Anonymous & Private)
* Stress Analytics Dashboard
* Wellness Resources

---

# Admin Features:

* User Monitoring
* Prediction Logs
* Model Performance Tracking
* Secure Admin Dashboard

---

#Output Screens:

* Landing Page
* Signup & Login
* Dashboard with Charts
* Questionnaire Page
* ML Prediction Page
* Tasks & Journal
* Resources Page

---

## 🔒 Security Features

* Password hashing
* Session-based authentication
* User data isolation
* Admin-only access controls

---

## 🚀 Future Enhancements

* Wearable device integration
* Real-time stress monitoring
* Deep Learning models (LSTM, CNN)
* Mobile App (Android/iOS)
* Voice & facial emotion analysis
* Multi-language support
* Cloud deployment (AWS / GCP)

---

## 👨‍👩‍👧 Team Members

| Name                    | Role                     |
| ----------------------- | ------------------------ |
| Aamir Husain            | Testing & Documentation  |
| Kutbuddin Bohra         | Frontend & Dashboard     |
| Pragati Vishwakarma     | Backend & ML Integration |


---

