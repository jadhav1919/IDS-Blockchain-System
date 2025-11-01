---

PROJECT TITLE: Blockchain-Based Collaborative Intrusion Detection System (BCI Experiments)

This project simulates a Blockchain-integrated Intrusion Detection System (IDS) that enables multiple nodes (RSPs) to collaboratively detect cyber attacks and record alerts on a tamper-proof blockchain.
It also provides a real-time Cyber Defense Dashboard to visualize alerts and blockchain transactions.

---

## FEATURES

1. Multiple IDS nodes (node1.py, node2.py, node3.py)
2. Machine Learning–based attack detection
3. Blockchain integration for secure alert recording
4. IPFS support for decentralized alert storage
5. Real-time Cyber Defense Dashboard (blockchain_server.py)
6. Coordinator module for node communication
7. Log storage and visualization of attack alerts

---

## PROJECT STRUCTURE

train_models.py        -> Trains ML models for intrusion detection
ids_node.py            -> Base IDS logic
node1.py, node2.py, node3.py -> Individual IDS node scripts
blockchain.py, blockchain_module.py -> Blockchain logic (block creation, validation)
blockchain_server.py   -> Flask web server + Dashboard UI
coordinator.py         -> System manager to coordinate IDS nodes
alerts.log             -> Stores all real-time alerts
models/                -> Saved ML models
preprocessed/, dataset/ -> Data used for training/testing
predict_realtime.py    -> Simulates real-time traffic and predictions
venv/                  -> Python virtual environment
logs/, results/        -> Output directories

---

## INSTALLATION

STEP 1: Clone and Enter Directory
git clone [https://github.com/jadhav1919/bci_experiments.git](https://github.com/jadhav1919/bci_experiments.git)
cd bci_experiments

STEP 2: Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

STEP 3: Install Dependencies
pip install flask joblib scikit-learn numpy pandas matplotlib

STEP 4 (Optional): Install IPFS for Decentralized Storage
sudo apt install ipfs
ipfs init
ipfs daemon

---

## DEMONSTRATION STEPS

STEP 1 — Train Models
python3 train_models.py

STEP 2 — Start Blockchain Dashboard
If port 5050 is free:
python3 blockchain_server.py
If port 5050 is in use:
python3 blockchain_server.py --port 5051
Then open your browser and go to:
[http://localhost:5050](http://localhost:5050)

STEP 3 — Start the Coordinator (System Manager)
python3 coordinator.py

STEP 4 — Start IDS Nodes
Open three new terminals and run:
python3 node1.py
python3 node2.py
python3 node3.py

Each node will detect simulated attacks and push alerts to:

* Blockchain
* IPFS (optional)
* alerts.log
* Dashboard UI

STEP 5 — View Real-Time Alerts
Open your browser and go to:
[http://localhost:5050](http://localhost:5050)
You will see:

* Real-time cyber alerts
* Blockchain transactions
* Node activity feed

---

## TROUBLESHOOTING

Problem: Port 5050 already in use
Solution: Run with --port 5051 or --port 5052

Problem: Error: someone else has the IPFS lock
Solution: Stop existing IPFS daemon using: pkill ipfs

Problem: ModuleNotFoundError: No module named 'joblib'
Solution: Run: pip install joblib inside your virtual environment

Problem: No alerts.log found
Solution: Start IDS nodes first before running the dashboard

---

## OPTIONAL ENHANCEMENTS

1. Add charts for attack frequency and node activity
2. Add node health status panel (RSP1–RSP3)
3. Extend blockchain to include smart contracts in /contracts/
4. Store full alert data on IPFS for immutable forensic evidence

---

## AUTHOR

Name: Jadhav Sai
College: Indian Institute of Information Technology, Kottayam
LinkedIn: [https://www.linkedin.com/in/jadhav-sai](https://www.linkedin.com/in/jadhav-sai)
GitHub: [https://github.com/jadhav1919](https://github.com/jadhav1919)


