# 🔍 Python Port Scanner

A lightweight Python-based network port scanner that detects open ports 
and identifies running services on a target system.

## 📌 Features

- Scans ports 1–1024 on any target IP or hostname
- Identifies common services (FTP, SSH, HTTP, HTTPS, RDP, etc.)
- Flags dangerous open ports (e.g. Telnet on port 23)
- Displays timestamp of scan start
- Reports total number of open ports found

## 🛠️ Tools & Technologies

- Python 3
- Socket library
- Datetime library

## 🚀 How to Run

```bash
python port_scanner.py
Enter the target IP address: scanme.nmap.org

Scanning scanme.nmap.org...
Started: 2026-07-10 08:35:50

[OPEN] Port 21  - FTP
[OPEN] Port 22  - SSH
[OPEN] Port 80  - HTTP
[OPEN] Port 110 - POP3 (Email)
[OPEN] Port 443 - HTTPS

## 📸 Screenshot
![Port Scanner Output](Python-port-scanning.py.jpeg .jpeg)
Scan completed. 5 open ports found.

⚠️ Legal Disclaimer

This tool is intended for educational purposes and authorized
security testing only. Only scan systems you own or have explicit
permission to test. Unauthorized port scanning may be illegal.

🔗 Author

Ugochukwu Daniel Iwuoha SOC Analyst | Cybersecurity
