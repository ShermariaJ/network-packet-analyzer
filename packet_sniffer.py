# Import necessary functions from Scapy
# pyre-ignore[21]
from scapy.all import sniff, IP, TCP, UDP


# Function that runs whenever a packet is captured
def packet_callback(packet):

    # Check if the packet contains an IP layer
    if packet.haslayer(IP):

        source = packet[IP].src
        destination = packet[IP].dst

        print("Packet Captured")
        print(f"Source IP: {source}")
        print(f"Destination IP: {destination}")
        print("-" * 40)


print("Starting packet capture...\n")

# Capture 10 packets
sniff(prn=packet_callback, count=10)
