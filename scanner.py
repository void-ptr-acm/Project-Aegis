import socket
import sys
from datetime import datetime


def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN on {ip}")
        s.close()
    except Exception as e:
        pass

if __name__ == "__main__":
    print(f"[*] Scanner initialized at {datetime.now()}")
    print("[-] Error: Insufficient privileges. Run as root.")
    sys.exit(1)
