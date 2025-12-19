"""
ML Predictor module for stress detection
Loads the trained Random Forest model and makes predictions
"""
import os
import json
import pickle
import numpy as np

class StressPredictor:
    def __init__(self):
        self.model = None
        self.labels = {0: "Amused", 1: "Neutral", 2: "Stressed"}
        self.features = [
            'BVP_mean', 'BVP_std', 'EDA_phasic_mean', 'EDA_phasic_min', 'EDA_smna_min', 
            'EDA_tonic_mean', 'Resp_mean', 'Resp_std', 'TEMP_mean', 'TEMP_std', 'TEMP_slope',
            'BVP_peak_freq', 'age', 'height', 'weight'
        ]
        self.load_model()
    
    def load_model(self):
        """Load the trained model and labels"""
        model_path = os.path.join(os.path.dirname(__file__), 'model', 'stress_model.joblib')
        labels_path = os.path.join(os.path.dirname(__file__), 'model', 'labels.json')
        features_path = os.path.join(os.path.dirname(__file__), 'model', 'features.json')
        
        try:
            # Load model
            if os.path.exists(model_path):
                with open(model_path, 'rb') as f:
                    self.model = pickle.load(f)
                print(f"Model loaded successfully from {model_path}")
            else:
                print(f"Model file not found at {model_path}")
                return False
            
            # Load labels
            if os.path.exists(labels_path):
                with open(labels_path, 'r') as f:
                    labels_dict = json.load(f)
                    # Convert string keys to int
                    self.labels = {int(k): v for k, v in labels_dict.items()}
            
            # Load features
            if os.path.exists(features_path):
                with open(features_path, 'r') as f:
                    self.features = json.load(f)
            
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    
    def predict(self, features_dict):
        """
        Predict stress level from physiological features
        
        Args:
            features_dict: Dictionary with feature names as keys
        
        Returns:
            tuple: (predicted_label, confidence_scores)
        """
        if self.model is None:
            return "Model not loaded", None
        
        try:
            # Extract features in the correct order
            feature_values = [features_dict.get(feat, 0) for feat in self.features]
            feature_array = np.array(feature_values).reshape(1, -1)
            
            # Make prediction
            prediction = self.model.predict(feature_array)[0]
            probabilities = self.model.predict_proba(feature_array)[0]
            
            # Get label
            predicted_label = self.labels.get(int(prediction), "Unknown")
            
            # Create confidence dict
            confidence = {self.labels[i]: float(prob) for i, prob in enumerate(probabilities)}
            
            return predicted_label, confidence
        except Exception as e:
            print(f"Prediction error: {e}")
            return "Prediction error", None
    
    def is_loaded(self):
        """Check if model is loaded"""
        return self.model is not None
    
    def get_required_features(self):
        """Get list of required features"""
        return self.features.copy()

# Global predictor instance
_predictor = None

def get_predictor():
    """Get or create the global predictor instance"""
    global _predictor
    if _predictor is None:
        _predictor = StressPredictor()
    return _predictor
