import socket
import datetime

target = input("Enter the target IP address: ")
print(f"\nScanning {target}...")
print(f"Started: {datetime.datetime.now()}\n")

services = {
    21: "FTP", 22: "SSH", 23: "Telnet (DANGEROUS)",
    80: "HTTP", 443: "HTTPS", 3389: "RDP", 8080: "HTTP-Alt"
}

open_ports = []

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if s.connect_ex((target, port)) == 0:
        service = services.get(port, "Unknown")
        print(f"[OPEN] Port {port} - {service}")
        open_ports.append(port)
    s.close()

print(f"\nScan completed. {len(open_ports)} open ports found.")

