"""
Setup script to train the ML model and prepare the Django app
Run this after installing requirements
"""
import os
import sys
import subprocess

def main():
    print("=" * 60)
    print("ML Stress Detection Setup")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("Error: Please run this script from the stress_project_extended directory")
        sys.exit(1)
    
    # Step 1: Run migrations
    print("\n[1/3] Running Django migrations...")
    try:
        subprocess.run([sys.executable, 'manage.py', 'makemigrations'], check=True)
        subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
        print("✓ Migrations completed")
    except subprocess.CalledProcessError as e:
        print(f"✗ Migration failed: {e}")
        return
    
    # Step 2: Train the model
    print("\n[2/3] Training the ML model...")
    model_dir = os.path.join('predictor', 'model')
    train_script = os.path.join(model_dir, 'train_model.py')
    
    if not os.path.exists(train_script):
        print(f"✗ Training script not found at {train_script}")
        return
    
    # Change to model directory to run training
    original_dir = os.getcwd()
    try:
        os.chdir(model_dir)
        subprocess.run([sys.executable, 'train_model.py'], check=True)
        print("✓ Model training completed")
    except subprocess.CalledProcessError as e:
        print(f"✗ Model training failed: {e}")
        print("Make sure the data file exists at: model/data/merged.csv")
        return
    except Exception as e:
        print(f"✗ Error: {e}")
        return
    finally:
        os.chdir(original_dir)
    
    # Step 3: Verify model files
    print("\n[3/3] Verifying model files...")
    model_file = os.path.join(model_dir, 'stress_model.joblib')
    labels_file = os.path.join(model_dir, 'labels.json')
    features_file = os.path.join(model_dir, 'features.json')
    
    if os.path.exists(model_file):
        print(f"✓ Model file created: {model_file}")
    else:
        print(f"✗ Model file not found: {model_file}")
    
    if os.path.exists(labels_file):
        print(f"✓ Labels file created: {labels_file}")
    else:
        print(f"✗ Labels file not found: {labels_file}")
    
    if os.path.exists(features_file):
        print(f"✓ Features file created: {features_file}")
    else:
        print(f"✗ Features file not found: {features_file}")
    
    print("\n" + "=" * 60)
    print("Setup Complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Create a superuser: python manage.py createsuperuser")
    print("2. Run the server: python manage.py runserver")
    print("3. Visit http://localhost:8000 and sign up/login")
    print("4. Navigate to 'ML Prediction' to test the model")
    print("=" * 60)

if __name__ == '__main__':
    main()
