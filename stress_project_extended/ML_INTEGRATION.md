# ML Model Integration Documentation

## Overview

This document explains how the ML model from `model/model.ipynb` has been integrated into the Django application.

## Architecture

### 1. Model Training (`predictor/model/train_model.py`)
- Loads data from `../model/data/merged.csv`
- Trains a Random Forest classifier
- Saves the model as `stress_model.joblib`
- Exports labels and feature names as JSON files

### 2. Prediction Module (`predictor/ml_predictor.py`)
- `StressPredictor` class handles model loading and predictions
- Singleton pattern via `get_predictor()` function
- Loads model, labels, and features on initialization
- Provides `predict()` method for making predictions

### 3. Django Models (`predictor/models.py`)
- `PhysiologicalData` model stores sensor data and predictions
- Fields for all 15 features used by the ML model
- Stores prediction results and confidence scores

### 4. Django Forms (`predictor/forms.py`)
- `PhysiologicalDataForm` for collecting sensor data
- User-friendly labels and placeholders
- Input validation and formatting

### 5. Django Views (`predictor/views.py`)
- `ml_predict_view()` handles the prediction workflow
- Collects data, makes prediction, saves results
- Displays results with confidence scores

### 6. Templates
- `ml_predict.html` - Data input form
- `ml_result.html` - Prediction results display
- `dashboard.html` - Updated to show ML predictions

## Data Flow

```
User Input (Form)
    ↓
PhysiologicalDataForm
    ↓
ml_predict_view()
    ↓
StressPredictor.predict()
    ↓
Random Forest Model
    ↓
Prediction + Confidence Scores
    ↓
Save to Database
    ↓
Display Results
```

## Features Used by the Model

The model requires 15 features in this exact order:

1. **BVP_mean** - Blood Volume Pulse mean
2. **BVP_std** - Blood Volume Pulse standard deviation
3. **BVP_peak_freq** - Blood Volume Pulse peak frequency
4. **EDA_phasic_mean** - Electrodermal Activity phasic component mean
5. **EDA_phasic_min** - Electrodermal Activity phasic component minimum
6. **EDA_smna_min** - Electrodermal Activity SMNA minimum
7. **EDA_tonic_mean** - Electrodermal Activity tonic component mean
8. **Resp_mean** - Respiration mean
9. **Resp_std** - Respiration standard deviation
10. **TEMP_mean** - Temperature mean
11. **TEMP_std** - Temperature standard deviation
12. **TEMP_slope** - Temperature slope
13. **age** - User age
14. **height** - User height in cm
15. **weight** - User weight in kg

## Prediction Classes

The model predicts one of three stress levels:

- **0: Amused** - Relaxed, positive emotional state
- **1: Neutral** - Baseline, normal state
- **2: Stressed** - High stress, negative emotional state

## Model Performance

- **Algorithm**: Random Forest Classifier
- **Training Accuracy**: ~96%
- **Features**: 15 physiological and demographic features
- **Dataset**: WESAD (Wearable Stress and Affect Detection)

## Code Examples

### Making a Prediction

```python
from predictor.ml_predictor import get_predictor

# Get predictor instance
predictor = get_predictor()

# Prepare features
features = {
    'BVP_mean': 0.025,
    'BVP_std': 0.015,
    'BVP_peak_freq': 1.2,
    'EDA_phasic_mean': 0.05,
    'EDA_phasic_min': 0.01,
    'EDA_smna_min': 0.02,
    'EDA_tonic_mean': 0.1,
    'Resp_mean': 0.3,
    'Resp_std': 0.05,
    'TEMP_mean': 32.5,
    'TEMP_std': 0.2,
    'TEMP_slope': 0.001,
    'age': 27,
    'height': 175,
    'weight': 70
}

# Make prediction
label, confidence = predictor.predict(features)

print(f"Predicted: {label}")
print(f"Confidence: {confidence}")
```

### Saving to Database

```python
from predictor.models import PhysiologicalData

data = PhysiologicalData(
    user=request.user,
    BVP_mean=0.025,
    # ... other features ...
    predicted_level=label,
    confidence_amused=confidence['Amused'],
    confidence_neutral=confidence['Neutral'],
    confidence_stressed=confidence['Stressed']
)
data.save()
```

## Integration Points

### 1. Model Loading
- Model is loaded once when the Django app starts
- Singleton pattern ensures efficient memory usage
- Graceful fallback if model file is missing

### 2. Database Schema
- `PhysiologicalData` model stores all sensor readings
- Includes prediction results and confidence scores
- Linked to Django User model for tracking

### 3. User Interface
- Form with organized sections (BVP, EDA, Respiration, Temperature, Demographics)
- Sample data provided for testing
- Visual confidence scores with progress bars
- Color-coded results (green=Amused, yellow=Neutral, red=Stressed)

### 4. Dashboard Integration
- Shows recent ML predictions
- Displays confidence scores
- Model status indicator
- Quick access to new predictions

## File Locations

```
stress_project_extended/
├── predictor/
│   ├── model/
│   │   ├── train_model.py          # Training script
│   │   ├── stress_model.joblib     # Trained model (generated)
│   │   ├── labels.json             # Class labels (generated)
│   │   └── features.json           # Feature list (generated)
│   ├── ml_predictor.py             # Prediction logic
│   ├── models.py                   # PhysiologicalData model
│   ├── views.py                    # ml_predict_view
│   ├── forms.py                    # PhysiologicalDataForm
│   └── urls.py                     # URL routing
├── templates/predictor/
│   ├── ml_predict.html             # Input form
│   ├── ml_result.html              # Results page
│   └── dashboard.html              # Dashboard with ML section
└── model/                          # Original notebook location
    ├── model.ipynb                 # Original training notebook
    └── data/
        └── merged.csv              # Training dataset
```

## Testing

### Run Model Test
```cmd
python test_model.py
```

This will:
1. Load the trained model
2. Make a prediction with sample data
3. Display results and confidence scores

### Manual Testing
1. Start the server: `python manage.py runserver`
2. Login to the application
3. Navigate to "ML Prediction"
4. Enter sample data (provided on the form)
5. Submit and view results

## Troubleshooting

### Model Not Loading
**Symptom**: "Model not available" message on dashboard

**Solution**:
1. Run `python setup_ml.py` to train the model
2. Verify `predictor/model/stress_model.joblib` exists
3. Check console for error messages

### Prediction Errors
**Symptom**: "Prediction error" in results

**Solution**:
1. Verify all 15 features are provided
2. Check feature values are numeric
3. Ensure model file is not corrupted

### Import Errors
**Symptom**: Module not found errors

**Solution**:
1. Activate virtual environment
2. Install requirements: `pip install -r requirements.txt`
3. Verify Django settings are correct

## Future Enhancements

1. **Real-time Sensor Integration**
   - Connect to wearable devices
   - Stream data directly to the model
   - Continuous monitoring

2. **Model Retraining**
   - Collect user feedback
   - Retrain with new data
   - Improve accuracy over time

3. **API Endpoints**
   - REST API for predictions
   - Mobile app integration
   - Third-party service integration

4. **Advanced Analytics**
   - Trend analysis
   - Personalized insights
   - Stress pattern detection

5. **Multiple Models**
   - Compare different algorithms
   - Ensemble predictions
   - Model selection based on user data

## References

- Original Notebook: `model/model.ipynb`
- Dataset: WESAD (Wearable Stress and Affect Detection)
- Algorithm: Scikit-learn Random Forest Classifier
- Framework: Django 4.2+
