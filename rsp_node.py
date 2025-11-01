# rsp_node.py
import joblib, json, time, requests, numpy as np, argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--node", default="RSP1", help="Node name (RSP1,RSP2,...)")
parser.add_argument("--server", default="http://127.0.0.1:5000", help="Blockchain server URL")
parser.add_argument("--mode", choices=["simulate","from_test"], default="simulate", help="simulate random packets or use X_test.npy")
parser.add_argument("--count", type=int, default=20, help="how many packets to process")
args = parser.parse_args()

MODEL_PATH = "models/BCIDF_model.joblib"
SCALER_PATH = "scaler.pkl"

# load model + scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# optional: load X_test if using real test samples
if args.mode == "from_test":
    X_test = np.load("X_test.npy")

def post_alert(server_url, payload):
    try:
        r = requests.post(server_url + "/alert", json=payload, timeout=5)
        if r.status_code == 201:
            print(f"[{payload['node']}] Posted alert -> block #{r.json()['block']['index']}")
        else:
            print(f"[{payload['node']}] Server response: {r.status_code} {r.text}")
    except Exception as e:
        print(f"[{payload['node']}] Error posting: {e}")

print(f"Starting node {args.node} -> sending to {args.server} (mode={args.mode})")
for i in range(args.count):
    # prepare packet
    if args.mode == "simulate":
        packet = np.random.rand(1, 122)  # must match feature count used during training
    else:
        idx = i % len(X_test)
        packet = X_test[idx].reshape(1, -1)

    # scale & predict
    scaled = scaler.transform(packet)
    pred = int(model.predict(scaled)[0])
    proba = float(max(model.predict_proba(scaled)[0]))

    # prepare alert if attack
    if pred == 1:
        alert = {
            "node": args.node,
            "packet_id": int(time.time()*1000) % 1000000,
            "prediction": "Attack",
            "confidence": proba,
            "timestamp": datetime.utcnow().isoformat()+"Z"
        }
        post_alert(args.server, alert)
    else:
        print(f"[{args.node}] Packet #{i+1}: normal")

    time.sleep(0.8)  # simulate arrival rate
