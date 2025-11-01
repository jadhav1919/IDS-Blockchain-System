#!/bin/bash

echo " Launching 3 IDS Nodes (RSPs) in separate terminals..."

gnome-terminal -- bash -c "source venv/bin/activate; python3 node1.py; exec bash"
sleep 1

gnome-terminal -- bash -c "source venv/bin/activate; python3 node2.py; exec bash"
sleep 1

gnome-terminal -- bash -c "source venv/bin/activate; python3 node3.py; exec bash"
sleep 1

echo "All IDS nodes are running in separate terminals!"
