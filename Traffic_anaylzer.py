from scapy.all import *
import time

def analyze_packet(packet):
    if packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"TCP Packet: {src_ip} -> {dst_ip}")
        # Detect repeated login attempts (e.g., port 80 for HTTP)
        if packet[TCP].dport == 80:
            print("Possible login attempt on port 80!")

print("Starting packet capture... Press Ctrl+C to stop.")
sniff(prn=analyze_packet, filter="tcp", store=0)
