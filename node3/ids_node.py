import joblib, numpy as np, socket, json, random, time

SERVER_HOST = 'localhost'   # coordinator machine
SERVER_PORT = 9001          # must match coordinator port

print("🚀 IDS Node Started… Loading Model…")
model = joblib.load('models/BCIDF_model.joblib')
print("✅ Model Loaded Successfully!\n")

sock = socket.socket()
sock.connect((SERVER_HOST, SERVER_PORT))
print("📡 Connected to Coordinator.\n")

for round_no in range(1, 6):
    # generate random network-like features (example shape of 10 features)
    features = np.random.rand(1, 10)
    prediction = model.predict(features)[0]
    result = "Attack" if prediction == 1 else "Normal"

    message = json.dumps({"node": "Node-3", "round": round_no, "result": result})
    sock.send(message.encode())
    print(f"[Round {round_no}] Sent → {result}")
    time.sleep(2)

sock.close()
print("\n✅ IDS Node Completed!")
