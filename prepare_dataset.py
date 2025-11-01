# prepare_dataset.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
import joblib
import os

# ---------------------------
# 1 Load training and test data
# ---------------------------
train_path = "dataset/KDDTrain+.txt"
test_path = "dataset/KDDTest+.txt"

df_train = pd.read_csv(train_path, header=None)
df_test = pd.read_csv(test_path, header=None)

print("Train shape:", df_train.shape)
print("Test shape:", df_test.shape)

# ---------------------------
# 2 Combine train + test for consistent preprocessing
# ---------------------------
df = pd.concat([df_train, df_test], axis=0)

# The last two columns in KDD = label and difficulty level
labels = df.iloc[:, -2]  # Second last column = attack type
difficulty = df.iloc[:, -1]  # Last column (we’ll drop this)

# Binary encode labels: normal=0, attack=1
y = labels.apply(lambda x: 0 if x == 'normal' else 1)
df['label'] = y

# Features = all except last two original columns
X = df.iloc[:, :-3]  # drop label + difficulty columns
print("Features shape:", X.shape)

# ---------------------------
# 3 Handle categorical features
# ---------------------------
categorical_cols = [1, 2, 3]  # protocol_type, service, flag
X_encoded = pd.get_dummies(X, columns=categorical_cols)
X_encoded.columns = X_encoded.columns.astype(str)  # ensure all column names are strings

# ---------------------------
# 4 Normalize numeric data
# ---------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)
print("Scaled shape:", X_scaled.shape)

# ---------------------------
# 5 Create balanced dataset (optional)
# ---------------------------
df_scaled = pd.DataFrame(X_scaled, columns=X_encoded.columns)
df_scaled['label'] = df['label'].values

df_majority = df_scaled[df_scaled.label == 1]
df_minority = df_scaled[df_scaled.label == 0]

if len(df_minority) > 0:
    df_minority_upsampled = resample(
        df_minority,
        replace=True,
        n_samples=len(df_majority),
        random_state=42
    )
    df_balanced = pd.concat([df_majority, df_minority_upsampled])
    print(" Resampling done. Balanced dataset created.")
else:
    print(" Only one class found. Skipping resampling step.")
    df_balanced = df_majority

print("Final balanced shape:", df_balanced.shape)

# ---------------------------
# 6 Train-test split
# ---------------------------
X_final = df_balanced.drop('label', axis=1)
y_final = df_balanced['label']

X_train, X_test, y_train, y_test = train_test_split(
    X_final, y_final, test_size=0.3, random_state=42,
    stratify=y_final if len(np.unique(y_final)) > 1 else None
)

print("Train size:", X_train.shape[0])
print("Test size:", X_test.shape[0])
print("Labels in test set:", np.unique(y_test, return_counts=True))

# ---------------------------
# 7 Save preprocessed data
# ---------------------------
os.makedirs("preprocessed", exist_ok=True)
joblib.dump((X_train, X_test, y_train, y_test), "preprocessed/data_split.joblib")
joblib.dump(scaler, "preprocessed/scaler.pkl")

print(" Preprocessed data saved in 'preprocessed/' folder.")

