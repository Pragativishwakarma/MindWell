"""
Train the stress detection model from the notebook data
and save it in the format expected by Django
"""
import numpy as np
import pandas as pd
import pickle
import json
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Path to the data file
DATA_PATH = os.path.join('..', '..', '..', 'model', 'data', 'merged.csv')

# Load the dataset
df = pd.read_csv(DATA_PATH, index_col=0)

# Selected features from the notebook
selected_feats = [
    'BVP_mean', 'BVP_std', 'EDA_phasic_mean', 'EDA_phasic_min', 'EDA_smna_min', 
    'EDA_tonic_mean', 'Resp_mean', 'Resp_std', 'TEMP_mean', 'TEMP_std', 'TEMP_slope',
    'BVP_peak_freq', 'age', 'height', 'weight'
]

X = df[selected_feats]
y = df['label']

# Split the data
X_train, X_test = train_test_split(X, test_size=0.1, random_state=0)
y_train, y_test = train_test_split(y, test_size=0.1, random_state=0)

# Train the model
print("Training Random Forest model...")
model = RandomForestClassifier(random_state=0)
model.fit(X_train, y_train)

# Test accuracy
accuracy = model.score(X_test, y_test) * 100
print(f"Model accuracy: {accuracy:.2f}%")

# Save the model using pickle (compatible with joblib)
model_path = 'stress_model.joblib'
with open(model_path, 'wb') as f:
    pickle.dump(model, f)
print(f"Model saved to {model_path}")

# Save labels mapping
labels = {
    0: "Amused",
    1: "Neutral", 
    2: "Stressed"
}

labels_path = 'labels.json'
with open(labels_path, 'w') as f:
    json.dump(labels, f)
print(f"Labels saved to {labels_path}")

# Save feature names for reference
features_path = 'features.json'
with open(features_path, 'w') as f:
    json.dump(selected_feats, f)
print(f"Features saved to {features_path}")

print("\nModel training complete!")
print(f"Features used: {len(selected_feats)}")
print(f"Classes: {list(labels.values())}")
