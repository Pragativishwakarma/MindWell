# ML Stress Detection - Setup Guide

This guide will help you integrate the trained ML model from `model/model.ipynb` with the Django application.

## Overview

The system uses a Random Forest classifier trained on physiological sensor data (BVP, EDA, Respiration, Temperature) to predict stress levels:
- **Amused** (relaxed/positive state)
- **Neutral** (baseline state)
- **Stressed** (high stress state)

## Prerequisites

- Python 3.8 or higher
- The dataset file at `../model/data/merged.csv`

## Installation Steps

### 1. Activate Virtual Environment (if not already active)

**Windows:**
```cmd
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 2. Install Required Packages

```cmd
pip install -r requirements.txt
```

This will install:
- Django
- NumPy
- Pandas
- Scikit-learn
- Joblib

### 3. Run the Setup Script

```cmd
python setup_ml.py
```

This script will:
1. Run Django migrations to create the database tables
2. Train the ML model using data from `../model/data/merged.csv`
3. Save the trained model to `predictor/model/stress_model.joblib`
4. Create label and feature mapping files

### 4. Create a Superuser (Optional)

```cmd
python manage.py createsuperuser
```

### 5. Run the Development Server

```cmd
python manage.py runserver
```

Visit: http://localhost:8000

## Manual Model Training (Alternative)

If you prefer to train the model manually:

```cmd
cd predictor/model
python train_model.py
cd ../..
```

## Using the Application

### 1. Sign Up / Login
- Create a new account or login with existing credentials

### 2. ML Prediction
- Click "ML Prediction" in the navigation bar
- Enter physiological sensor data
- Click "Predict Stress Level"
- View results with confidence scores

### 3. Sample Data for Testing

Use these values from the training dataset:

```
BVP (Blood Volume Pulse):
- Mean: 0.025
- Std: 0.015
- Peak Frequency: 1.2

EDA (Electrodermal Activity):
- Phasic Mean: 0.05
- Phasic Min: 0.01
- SMNA Min: 0.02
- Tonic Mean: 0.1

Respiration:
- Mean: 0.3
- Std: 0.05

Temperature:
- Mean: 32.5
- Std: 0.2
- Slope: 0.001

Demographics:
- Age: 27
- Height: 175 cm
- Weight: 70 kg
```

### 4. View Dashboard
- See your prediction history
- View confidence scores for each prediction
- Track mood entries and questionnaire responses

## Features

### ML-Based Prediction
- Uses 15 physiological features
- Random Forest classifier with ~96% accuracy
- Provides confidence scores for each class

### Questionnaire-Based Assessment
- 10-question stress assessment
- Rule-based scoring system
- Quick stress level estimation

### Mood Tracking
- Daily mood entries (1-10 scale)
- Notes and observations
- Historical tracking

### Task Management
- Create and manage daily tasks
- Set due dates
- Mark tasks as complete

### Journal
- Private or anonymous entries
- Share experiences
- View community entries

### Resources
- Relaxation exercises
- Stress management articles
- Emergency helplines

## File Structure

```
stress_project_extended/
├── predictor/
│   ├── model/
│   │   ├── train_model.py      # Model training script
│   │   ├── stress_model.joblib # Trained model (generated)
│   │   ├── labels.json         # Class labels (generated)
│   │   └── features.json       # Feature names (generated)
│   ├── ml_predictor.py         # Prediction module
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── forms.py                # Form definitions
│   └── urls.py                 # URL routing
├── templates/
│   └── predictor/
│       ├── ml_predict.html     # ML prediction form
│       ├── ml_result.html      # Prediction results
│       └── dashboard.html      # User dashboard
├── manage.py
├── setup_ml.py                 # Setup automation script
└── requirements.txt
```

## Model Details

### Features Used (15 total)
1. BVP_mean, BVP_std, BVP_peak_freq
2. EDA_phasic_mean, EDA_phasic_min, EDA_smna_min, EDA_tonic_mean
3. Resp_mean, Resp_std
4. TEMP_mean, TEMP_std, TEMP_slope
5. age, height, weight

### Model Performance
- Algorithm: Random Forest Classifier
- Accuracy: ~96% on test set
- Classes: Amused (0), Neutral (1), Stressed (2)

## Troubleshooting

### Model Not Loading
- Ensure `stress_model.joblib` exists in `predictor/model/`
- Check that the training script completed successfully
- Verify the data file path is correct

### Import Errors
- Make sure all packages are installed: `pip install -r requirements.txt`
- Activate the virtual environment

### Database Errors
- Run migrations: `python manage.py migrate`
- Delete `db.sqlite3` and run migrations again if needed

### Training Errors
- Verify the dataset exists at `../model/data/merged.csv`
- Check that the CSV has all required columns
- Ensure sufficient disk space for model file

## API Integration (Future)

The predictor module can be easily integrated with REST APIs:

```python
from predictor.ml_predictor import get_predictor

predictor = get_predictor()
result, confidence = predictor.predict(features_dict)
```

## Support

For issues or questions:
1. Check the console output for error messages
2. Verify all setup steps were completed
3. Ensure the dataset file is accessible
4. Check Django logs for detailed error information

## Credits

Developed as part of the AI-Ready Mental Wellness & Stress Monitoring System
Model trained on WESAD dataset features
