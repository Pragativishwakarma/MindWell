"""
Quick test script to verify the ML model is working
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stress_project.settings')
django.setup()

from predictor.ml_predictor import get_predictor

def test_model():
    print("=" * 60)
    print("Testing ML Model")
    print("=" * 60)
    
    # Get predictor instance
    predictor = get_predictor()
    
    # Check if model is loaded
    if not predictor.is_loaded():
        print("✗ Model is not loaded!")
        print("Please run: python setup_ml.py")
        return False
    
    print("✓ Model loaded successfully")
    
    # Test with sample data
    print("\nTesting with sample data...")
    sample_features = {
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
    predicted_label, confidence = predictor.predict(sample_features)
    
    print(f"\nPrediction Result: {predicted_label}")
    
    if confidence:
        print("\nConfidence Scores:")
        for label, score in confidence.items():
            print(f"  {label}: {score*100:.2f}%")
    
    print("\n✓ Model test completed successfully!")
    print("=" * 60)
    return True

if __name__ == '__main__':
    try:
        test_model()
    except Exception as e:
        print(f"\n✗ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
