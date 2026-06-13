import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# -----------------------------
# 1. LOAD DATA
# -----------------------------
data = pd.read_csv("electricity.csv")

# -----------------------------
# 2. CLEAN DATA
# -----------------------------

# Replace '?' with NaN
data.replace('?', np.nan, inplace=True)

# Convert columns to numeric
cols = [
    'ForecastWindProduction', 'SystemLoadEA', 'SMPEA',
    'ORKTemperature', 'ORKWindspeed', 'CO2Intensity',
    'ActualWindProduction', 'SystemLoadEP2', 'SMPEP2'
]

for col in cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Drop missing values
data.dropna(inplace=True)

# -----------------------------
# 3. HANDLE DATETIME
# -----------------------------
data['DateTime'] = pd.to_datetime(data['DateTime'], dayfirst=True)

data['hour'] = data['DateTime'].dt.hour
data['day'] = data['DateTime'].dt.day
data['month'] = data['DateTime'].dt.month

# -----------------------------
# 4. DROP UNUSED COLUMNS
# -----------------------------
data.drop(['DateTime', 'Holiday'], axis=1, inplace=True)

# -----------------------------
# 5. DEFINE FEATURES & TARGET
# -----------------------------
X = data.drop('SMPEP2', axis=1)   # Features
y = data['SMPEP2']                # Target (Electricity Price)

# -----------------------------
# 6. TRAIN MODEL
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor()
model.fit(X_train, y_train)

# -----------------------------
# 7. SAVE MODEL
# -----------------------------
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained and saved as model.pkl")