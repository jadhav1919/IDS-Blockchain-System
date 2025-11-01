import time
import json
import joblib
import numpy as np
import random
from datetime import datetime
from colorama import Fore, Style, init
import warnings
import os

NODE_NAME = "Node-2"
MODEL_PATH = "models/BCIDF_model.joblib"
SCALER_PATH = "scaler.pkl"
ALERT_FILE = f"alert_{NODE_NAME.lower()}.json"

init(autoreset=True)
warnings.filterwarnings("ignore")

print(f"[{NODE_NAME}] Loading model and scaler...")
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

try:
    X_test = np.load("X_test.npy")
    print(f"[{NODE_NAME}] Loaded dataset with shape {X_test.shape}")
except:
    X_test = np.random.rand(100, 122)
    print(f"[{NODE_NAME}] Using random data.")

attack_labels = ["DoS", "Probe", "R2L", "U2R"]
print(f"[{NODE_NAME}] Simulation started.\n")

try:
    while True:
        idx = random.randint(0, len(X_test) - 1)
        packet = X_test[idx].reshape(1, -1)
        scaled = scaler.transform(packet)
        prediction = model.predict(scaled)[0]

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if prediction == 1:
            attack = random.choice(attack_labels)
            log = {"node": NODE_NAME, "timestamp": timestamp, "status": "Attack", "attack_type": attack}
            color = Fore.RED
            msg = f"🚨 Attack Detected ({attack})"
        else:
            log = {"node": NODE_NAME, "timestamp": timestamp, "status": "Normal"}
            color = Fore.BLUE
            msg = "🟦 Normal Traffic"

        print(f"{color}[{NODE_NAME}] {timestamp} → {msg}{Style.RESET_ALL}")

        with open(ALERT_FILE, "a", buffering=1) as f:
            f.write(json.dumps(log) + "\n")
            f.flush()
            os.fsync(f.fileno())

        time.sleep(2)
except KeyboardInterrupt:
    print(f"\n[{NODE_NAME}] Stopped.")

