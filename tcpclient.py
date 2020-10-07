#!/usr/bin/env python3

import socket

target_host = "0.0.0.0"

target_port = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send('Hello'.encode('utf-8'))

response = client.recv(4096).decode('utf-8')

print(response)
