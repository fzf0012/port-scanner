# Port Scanner & Banner Grabber

A simple yet effective Python-based tool to identify open TCP ports and perform banner grabbing for exposed services. Built as a personal project to emulate reconnaissance techniques used by adversaries, based on the [MITRE ATT&CK](https://attack.mitre.org/) framework.

---

## 📌 Features

- Scans TCP ports in a user-defined range
- Performs banner grabbing to detect services
- Emulates MITRE ATT&CK techniques:
  - T1046: Network Service Scanning
  - T1040: Network Sniffing *(future)*
- Command-line interface
- Built for ethical hacking in controlled lab environments

---

## 🧪 Demo

```bash
$ python3 scanner.py --target 192.168.1.100 --start-port 20 --end-port 1024
[INFO] Scanning host: 192.168.1.100
[+] Port 22 open: SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3
[+] Port 80 open: HTTP/1.1 200 OK
