#!/usr/bin/env python3
# filepath: /Users/mike/development/c/proxylab-handout/nop-server.py
"""
A do-nothing server that never responds to any requests.
Used to test proxy timeout capabilities.
"""

import socket
import sys
import signal
import time

def signal_handler(sig, frame):
    print('Exiting')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if len(sys.argv) != 2:
    print("Usage: {} <port>".format(sys.argv[0]))
    sys.exit(1)

port = int(sys.argv[1])
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('0.0.0.0', port))
server_socket.listen(5)

print(f"NOP-server listening on port {port}, intentionally not responding to connections")

while True:
    try:
        client_sock, client_addr = server_socket.accept()
        print(f"Connection accepted from {client_addr}, but not responding")
        while True:
            time.sleep(10)
    except Exception as e:
        print(f"Error: {e}")