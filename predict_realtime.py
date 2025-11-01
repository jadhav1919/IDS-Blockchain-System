import time
import random
import joblib
import numpy as np
import warnings
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init(autoreset=True)

# Suppress unnecessary warnings
warnings.filterwarnings("ignore")

print("\n🚀 Starting Real-Time Intrusion Detection Simulation...\n")

# Load model and scaler
model = joblib.load("models/BCIDF_model.joblib")
scaler = joblib.load("scaler.pkl")

print("✅ BCIDF model loaded successfully.\n")

# Counters for results
total_packets = 0
attack_count = 0
normal_count = 0

# Simulate real-time packet detection (10 samples)
for i in range(1, 11):
    total_packets += 1

    # Generate random packet (122 features same as training dataset)
    packet = np.random.rand(1, 122)
    scaled_packet = scaler.transform(packet)
    prediction = model.predict(scaled_packet)[0]

    if prediction == 1:
        attack_count += 1
        print(f"[{i}] Packet classified as: {Fore.RED}⚠️ Attack Detected{Style.RESET_ALL}")
    else:
        normal_count += 1
        print(f"[{i}] Packet classified as: {Fore.GREEN}✅ Normal Traffic{Style.RESET_ALL}")

    # Wait 1 second between packets to simulate real-time monitoring
    time.sleep(1)

# Display summary
print("\n📊 Simulation Summary:")
print(f"   Total Packets Processed : {total_packets}")
print(f"   {Fore.RED}Attacks Detected          : {attack_count}{Style.RESET_ALL}")
print(f"   {Fore.GREEN}Normal Packets            : {normal_count}{Style.RESET_ALL}")

print("\n🎉 Real-Time Detection Simulation Completed!\n")

