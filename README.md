# Network Packet Analyzer

## Overview
A Python-based network packet analyzer that captures and inspects network traffic using the Scapy library.

The tool monitors packets on the network and displays information such as protocol type, source IP, destination IP, and ports.

## Features
- Captures live network packets
- Detects TCP and UDP protocols
- Displays source and destination IP addresses
- Displays source and destination ports

## Usage

Run the program:

python packet_sniffer.py

Example output:

TCP Packet
192.168.1.4:52341 → 142.250.190.78:443

## Requirements
- Python 3.x
- Scapy

Install dependencies:

pip install -r requirements.txt
