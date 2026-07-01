# Blockchain-Based Collaborative Intrusion Detection System 

A Blockchain-integrated Intrusion Detection System (IDS) that enables multiple distributed IDS nodes to collaboratively detect cyber attacks and securely record alerts on an immutable blockchain.

The project also includes a real-time Cyber Defense Dashboard for monitoring network events, blockchain transactions, and IDS node activity.

> **Status:** Academic Research Project

---

# Overview

This project demonstrates how blockchain technology can improve the integrity and trustworthiness of intrusion detection systems.

Multiple IDS nodes independently monitor network traffic, detect malicious activity using machine learning models, and submit alerts to a blockchain where records become tamper-resistant and auditable.

The system also supports optional IPFS integration for decentralized alert storage.

---

# Key Features

- Distributed IDS architecture with multiple detection nodes
- Machine Learning-based intrusion detection
- Blockchain-based immutable alert logging
- Optional IPFS integration for decentralized storage
- Real-time Cyber Defense Dashboard
- Centralized coordinator for node communication
- Live monitoring of alerts and blockchain transactions
- Persistent alert logging for forensic analysis

---

# System Architecture

```
                    Network Traffic
                           │
        ┌──────────────────┴──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
     IDS Node 1        IDS Node 2        IDS Node 3
        │                  │                  │
        └──────────────┬───┴──────────────────┘
                       │
                 Coordinator
                       │
         ┌─────────────┴─────────────┐
         │                           │
         ▼                           ▼
     Blockchain                 IPFS Storage
         │                           │
         └─────────────┬─────────────┘
                       │
                       ▼
            Cyber Defense Dashboard
```

---

# Technologies Used

- Python 3
- Flask
- Scikit-learn
- NumPy
- Pandas
- Joblib
- Blockchain
- IPFS
- Machine Learning
- HTML/CSS
- JavaScript

---

# Project Structure

```
bci_experiments/
│
├── train_models.py
├── ids_node.py
├── node1.py
├── node2.py
├── node3.py
├── blockchain.py
├── blockchain_module.py
├── blockchain_server.py
├── coordinator.py
├── predict_realtime.py
├── alerts.log
│
├── models/
├── dataset/
├── preprocessed/
├── logs/
├── results/
└── README.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/jadhav1919/bci_experiments.git
cd bci_experiments
```

---

## 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```cmd
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install flask
pip install joblib
pip install scikit-learn
pip install numpy
pip install pandas
pip install matplotlib
```

or

```bash
pip install -r requirements.txt
```

---

## 4. Optional: Install IPFS

```bash
sudo apt install ipfs
ipfs init
ipfs daemon
```

---

# Running the Project

## Step 1 – Train the Machine Learning Models

```bash
python3 train_models.py
```

---

## Step 2 – Start the Blockchain Dashboard

```bash
python3 blockchain_server.py
```

If port **5050** is unavailable:

```bash
python3 blockchain_server.py --port 5051
```

Open your browser:

```
http://localhost:5050
```

---

## Step 3 – Start the Coordinator

```bash
python3 coordinator.py
```

---

## Step 4 – Launch IDS Nodes

Open three separate terminals.

Terminal 1

```bash
python3 node1.py
```

Terminal 2

```bash
python3 node2.py
```

Terminal 3

```bash
python3 node3.py
```

Each node continuously monitors simulated traffic and sends alerts to the blockchain.

---

## Step 5 – Monitor the Dashboard

Open:

```
http://localhost:5050
```

The dashboard displays:

- Real-time intrusion alerts
- Blockchain transactions
- IDS node activity
- Alert history
- System status

---

# Detection Workflow

```
Incoming Traffic
        │
        ▼
Machine Learning Detection
        │
        ▼
Attack Identified
        │
        ▼
Alert Generated
        │
        ▼
Blockchain Record Created
        │
        ▼
(Optional) Store Alert on IPFS
        │
        ▼
Display on Dashboard
```

---

# Troubleshooting

### Port Already in Use

```bash
python3 blockchain_server.py --port 5051
```

---

### IPFS Lock Error

```bash
pkill ipfs
```

Restart:

```bash
ipfs daemon
```

---

### Missing Python Package

```bash
pip install joblib
```

or

```bash
pip install -r requirements.txt
```

---

### alerts.log Not Found

Start the IDS nodes before opening the dashboard.

---

# Future Improvements

- Smart contract integration
- Consensus algorithms
- Attack severity visualization
- Interactive analytics dashboard
- Email and SMS alerting
- Docker deployment
- Kubernetes support
- REST API
- Threat intelligence integration
- SIEM integration

---

# Learning Outcomes

This project demonstrates practical experience with:

- Intrusion Detection Systems (IDS)
- Blockchain Security
- Machine Learning
- Cyber Defense Automation
- Flask Web Development
- Distributed Systems
- IPFS
- Security Monitoring
- Python Programming
- Real-time Event Processing

---

# Disclaimer

This project was developed for educational and cybersecurity research purposes only.

It should be used only in authorized environments and controlled laboratory settings.

---

# Author

**Jadhav Sai**

**B.Tech Computer Science (Cyber Security)**  
Indian Institute of Information Technology, Kottayam

GitHub: https://github.com/jadhav1919

LinkedIn: https://www.linkedin.com/in/jadhav-sai
