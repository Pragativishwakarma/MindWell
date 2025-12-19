# AI-Powered Mental Wellness & Stress Detection System:

An intelligent web-based application built using **Django and Machine Learning** to predict user stress levels based on **questionnaire responses, physiological parameters, and behavioral data**.
The system promotes early stress detection and mental wellness through real-time predictions, dashboards, and wellness tools.

## 🌟 Features:

Stress has become a major concern in modern lifestyles. This project uses **Machine Learning models** integrated with a **Django web application** to classify stress levels into:

* 🟢 Low Stress
* 🟡 Medium Stress
* 🔴 High Stress

### 🤖 ML-Based Stress Detection:

- Random Forest classifier with **95% accuracy**
- Analyzes 15 physiological features (BVP, EDA, Respiration, Temperature)
- Real-time predictions with confidence scores
- Trained on WESAD dataset

### 📊 Wellness Dashboard:

- Interactive stress trend visualization
- Mood tracking with historical data
- ML prediction history with confidence scores
- Comprehensive analytics

### 📝 Personal Journal:

- Private or anonymous entries
- Community sharing option
- Safe space for self-reflection

### ✅ Task Management:

- Create and organize daily tasks
- Set due dates and priorities
- Track completion status

### 😊 Mood Tracking:

- Daily mood scale (1-10)
- Notes and observations
- Pattern recognition over time

### 📚 Wellness Resources:

- Breathing exercises
- Stress management articles
- Professional support links

### Prerequisites:

- Python 3.8 or higher
- pip package manager

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

## 📂 Project Structure:

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
 
 
 

```

## 🎯 Usage:

### 1. Sign Up / Login
Create an account or login to access all features

### 2. ML Stress Prediction
- Navigate to "ML Prediction"
- Enter physiological sensor data
- Get instant stress level prediction with confidence scores

**Sample Data for Testing:**
```
BVP: mean=0.025, std=0.015, peak_freq=1.2
EDA: phasic_mean=0.05, phasic_min=0.01, smna_min=0.02, tonic_mean=0.1
Resp: mean=0.3, std=0.05
TEMP: mean=32.5, std=0.2, slope=0.001
Demographics: age=27, height=175, weight=70
```

### 3. Track Your Mood
- Add daily mood entries
- View mood history on dashboard
- Identify patterns over time

### 4. Manage Tasks
- Create daily tasks
- Set due dates
- Mark as complete

### 5. Journal Your Thoughts
- Write private or anonymous entries
- Share with community
- Reflect on your mental health journey

## 🧪 Testing

Test the ML model:
```cmd
cd stress_project_extended
python test_model.py
```

## 📊 ML Model Details

- **Algorithm**: Random Forest Classifier
- **Accuracy**: 94.92%
- **Features**: 15 physiological and demographic features
- **Classes**: 
  - Amused (relaxed/positive)
  - Neutral (baseline)
  - Stressed (high stress)

## 🛠️ Technologies Used

- **Backend**: Django 5.2
- **ML**: Scikit-learn, NumPy, Pandas
- **Frontend**: Bootstrap 5, Chart.js
- **Database**: SQLite
- **Model Format**: Joblib/Pickle

## 📖 Documentation

- `SETUP_GUIDE.md` - Detailed setup instructions
- `ML_INTEGRATION.md` - Technical integration details
- `QUICK_START.txt` - Quick reference guide

## 🔧 Troubleshooting

### Model Not Loading
```cmd
cd stress_project_extended
python setup_ml.py
```

### Database Errors
```cmd
python manage.py migrate
```

### Import Errors
```cmd
pip install -r requirements.txt
```

## 🎨 Features Highlights

- **Beautiful UI**: Modern gradient design with smooth animations
- **Responsive**: Works on desktop, tablet, and mobile
- **Real-time**: Instant ML predictions
- **Secure**: Login required, user data isolation
- **Interactive**: Charts and visualizations
- **Comprehensive**: All-in-one mental wellness platform

## 📝 License

This project is for educational and research purposes.

## 👨‍💻 Developer

Developed by Aamir Husain

## 🤝 Contributing

This is a research project. For questions or suggestions, please open an issue.

## 📞 Support

For issues:
1. Check console output for error messages
2. Review documentation files
3. Ensure all setup steps were completed
4. Verify dataset file is accessible

## 🌟 Acknowledgments

- WESAD dataset for training data
- Django framework
- Scikit-learn library
- Bootstrap for UI components

---

**Ready to improve your mental wellness? Get started now!**

```cmd
cd stress_project_extended
python manage.py runserver

```
## 🚀 Future Enhancements

* Wearable device integration
* Real-time stress monitoring
* Deep Learning models (LSTM, CNN)
* Mobile App (Android/iOS)
* Voice & facial emotion analysis
* Multi-language support
* Cloud deployment (AWS / GCP)


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
## 👨‍👩‍👧 Team Members

| Name                    | Role                     |
| ----------------------- | ------------------------ |
| Aamir Husain            | Testing & Documentation  |
| Kutbuddin Bohra         | Frontend & Dashboard     |
| Pragati Vishwakarma     | Backend & ML Integration |