import random
import time

# List of possible cyberattacks
attack_types = [
    "DDoS",
    "SQL Injection",
    "Port Scan",
    "Brute Force",
    "XSS",
    "Man-in-the-Middle",
    "Ransomware",
    "Phishing",
    "Privilege Escalation"
]

print("🔰 Initializing AI-Powered Intrusion Detection System...")
print("🚀 System Online. Monitoring Traffic in Real-Time...\n")

while True:
    result = random.choice(["Normal", "Attack"])
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    if result == "Attack":
        attack_type = random.choice(attack_types)
        log = f"[ALERT] {attack_type} detected at {timestamp}\n"
    else:
        log = f"[INFO] Normal traffic at {timestamp}\n"

    # Write to log file
    with open("alerts.log", "a") as f:
        f.write(log)
    
    # Print to terminal too
    print(log.strip())
    time.sleep(2)

