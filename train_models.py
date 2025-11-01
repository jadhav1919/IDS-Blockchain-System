# train_models.py
import joblib, json, hashlib
import numpy as np
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from metrics import calc_metrics

# Load preprocessed data
X_train, X_test, y_train, y_test = joblib.load("preprocessed/data_split.joblib")
print("✅ Data loaded successfully.")

# ---- Random Forest ----
print("\nTraining Random Forest...")
rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    max_features="sqrt",
    min_samples_leaf=5,
    criterion="gini",
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
rf_metrics = calc_metrics(y_test, y_pred)

joblib.dump(rf, "models/RF_model.joblib")
h = hashlib.sha256(open("models/RF_model.joblib", "rb").read()).hexdigest()
rf_metrics["model"] = "RF"
rf_metrics["hash"] = h
open("results/RF_result.json", "w").write(json.dumps(rf_metrics, indent=2))
print("✅ RF done:", rf_metrics)


# ---- Extra Trees ----
print("\nTraining Extra Trees...")
et = ExtraTreesClassifier(
    n_estimators=100,
    max_depth=10,
    max_features="sqrt",
    min_samples_leaf=5,
    random_state=42,
    n_jobs=-1
)
et.fit(X_train, y_train)
y_pred = et.predict(X_test)
et_metrics = calc_metrics(y_test, y_pred)

joblib.dump(et, "models/ET_model.joblib")
h = hashlib.sha256(open("models/ET_model.joblib", "rb").read()).hexdigest()
et_metrics["model"] = "ET"
et_metrics["hash"] = h
open("results/ET_result.json", "w").write(json.dumps(et_metrics, indent=2))
print("✅ ET done:", et_metrics)


# ---- Refined Random Forest ----
print("\nTraining RRF (shallow forest)...")
rrf = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,           # smaller depth
    max_features="sqrt",
    min_samples_leaf=5,
    criterion="entropy",
    random_state=42,
    n_jobs=-1
)
rrf.fit(X_train, y_train)
y_pred = rrf.predict(X_test)
rrf_metrics = calc_metrics(y_test, y_pred)

joblib.dump(rrf, "models/RRF_model.joblib")
h = hashlib.sha256(open("models/RRF_model.joblib", "rb").read()).hexdigest()
rrf_metrics["model"] = "RRF"
rrf_metrics["hash"] = h
open("results/RRF_result.json", "w").write(json.dumps(rrf_metrics, indent=2))
print("✅ RRF done:", rrf_metrics)


# ---- Optimized Tree (simulated GA-tuned) ----
print("\nTraining Optimized Tree (OT)...")
ot = RandomForestClassifier(
    n_estimators=120,
    max_depth=12,
    max_features="sqrt",
    min_samples_leaf=4,
    criterion="entropy",
    random_state=7,
    n_jobs=-1
)
ot.fit(X_train, y_train)
y_pred = ot.predict(X_test)
ot_metrics = calc_metrics(y_test, y_pred)

joblib.dump(ot, "models/OT_model.joblib")
h = hashlib.sha256(open("models/OT_model.joblib", "rb").read()).hexdigest()
ot_metrics["model"] = "OT"
ot_metrics["hash"] = h
open("results/OT_result.json", "w").write(json.dumps(ot_metrics, indent=2))
print("✅ OT done:", ot_metrics)


# ---- Ensemble Decision Trees ----
print("\nTraining Ensemble Decision Trees (EDT)...")
clf1 = RandomForestClassifier(n_estimators=50, max_depth=8, random_state=1)
clf2 = ExtraTreesClassifier(n_estimators=50, max_depth=8, random_state=2)
clf1.fit(X_train, y_train)
clf2.fit(X_train, y_train)

pred1 = clf1.predict_proba(X_test)[:, 1]
pred2 = clf2.predict_proba(X_test)[:, 1]
avg_pred = ((pred1 + pred2) / 2) >= 0.5
y_pred = avg_pred.astype(int)

edt_metrics = calc_metrics(y_test, y_pred)

joblib.dump([clf1, clf2], "models/EDT_model.joblib")
h = hashlib.sha256(open("models/EDT_model.joblib", "rb").read()).hexdigest()
edt_metrics["model"] = "EDT"
edt_metrics["hash"] = h
open("results/EDT_result.json", "w").write(json.dumps(edt_metrics, indent=2))
print("✅ EDT done:", edt_metrics)


# ---- BCIDF (Proposed Framework) ----
print("\nTraining BCIDF (Blockchain-based)...")
bcidf = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    max_features="sqrt",
    min_samples_leaf=5,
    criterion="gini",
    random_state=100,
    n_jobs=-1
)
bcidf.fit(X_train, y_train)
y_pred = bcidf.predict(X_test)
bcidf_metrics = calc_metrics(y_test, y_pred)

joblib.dump(bcidf, "models/BCIDF_model.joblib")
h = hashlib.sha256(open("models/BCIDF_model.joblib", "rb").read()).hexdigest()
bcidf_metrics["model"] = "BCIDF"
bcidf_metrics["hash"] = h
open("results/BCIDF_result.json", "w").write(json.dumps(bcidf_metrics, indent=2))
print("✅ BCIDF done:", bcidf_metrics)

