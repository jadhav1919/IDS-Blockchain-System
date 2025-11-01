import requests
import time
import json
import os
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

BLOCKCHAIN_SERVER = "http://127.0.0.1:5000"
NODE_LOGS = ["alert_node1.json", "alert_node2.json", "alert_node3.json"]

print(Fore.CYAN + "🚀 Coordinator Started — Collecting IDS Node Alerts...\n")

# Genesis block
blockchain = []
genesis_block = {
    "index": 1,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "data": "Genesis Block",
    "previous_hash": "0",
    "hash": "GENESIS_HASH"
}
blockchain.append(genesis_block)


def get_node_status(log_file):
    if not os.path.exists(log_file):
        return "NoData"
    try:
        with open(log_file, "r") as f:
            lines = f.readlines()
            if not lines:
                return "NoData"
            last_entry = json.loads(lines[-1])
            return last_entry.get("status", "Error")
    except Exception:
        return "Error"


round_no = 0
while True:
    round_no += 1
    print(Fore.CYAN + f"\n🔹 Round {round_no}: Checking node alerts...")

    node_results = [get_node_status(f) for f in NODE_LOGS]
    print(Fore.WHITE + "🧩 Node Results →", node_results)

    valid_results = [r for r in node_results if r in ["Normal", "Attack"]]
    if not valid_results:
        print(Fore.YELLOW + "⚠️ No valid data yet, waiting...")
        time.sleep(3)
        continue

    if valid_results.count("Attack") > len(valid_results) / 2:
        decision = "Attack Detected"
        color = Fore.RED
        icon = "🚨"
    else:
        decision = "Normal Traffic"
        color = Fore.BLUE
        icon = "🟦"

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(color + f"{icon} Decision → {decision}")

    # Append to alerts.log
    log_entry = f"[{ts}] {decision} | Nodes: {node_results}\n"
    with open("alerts.log", "a") as log_file:
        log_file.write(log_entry)

    # Keep a snapshot of last few alerts
    try:
        with open("alerts.log", "r") as f:
            all_lines = f.readlines()
        snapshot = all_lines[-50:]
    except:
        snapshot = [log_entry]

    # Add new block
    block = {
        "index": len(blockchain) + 1,
        "timestamp": ts,
        "data": decision,
        "previous_hash": blockchain[-1]["hash"],
        "hash": str(hash(decision + str(time.time()))),
        "details": {
            "node_results": node_results,
            "timestamp": ts,
            "alert_snapshot": snapshot
        }
    }
    blockchain.append(block)

    # Send to blockchain server
    try:
        resp = requests.post(f"{BLOCKCHAIN_SERVER}/add_block", json=block, timeout=5)
        if resp.status_code == 200:
            print(Fore.GREEN + "✅ Block successfully sent to blockchain server.")
        else:
            print(Fore.YELLOW + f"⚠️ Blockchain server response: {resp.status_code} {resp.text}")
    except Exception as e:
        print(Fore.RED + f"❌ Error sending block to blockchain server: {e}")

    time.sleep(5)

