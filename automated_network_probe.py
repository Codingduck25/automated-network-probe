import socket
import sys

target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1.5)

print(f"[*] Auditing the connection capability to"
      f" {target_host}:{target_port}")

result = client.connect_ex((target_host, target_port))

if result == 0:
    print(f"[+] Status: OPEN. Port {target_port} is actively accepting connections")
else:
    print(f"[-] Status: CLOSED. Port {target_port} is unavailable or rejecting data.")

    client.close()
