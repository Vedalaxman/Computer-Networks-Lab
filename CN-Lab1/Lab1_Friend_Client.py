import socket

SERVER_IP = input("Enter server IP: ")  # Enter your classmate's server IP
PORT = 5001

CLIENT_NAME = input("Enter your name: ")
CLIENT_INT = int(input("Enter an integer (1-100): "))

if 1 <= CLIENT_INT <= 100:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))
        s.sendall(f"{CLIENT_NAME},{CLIENT_INT}".encode())
        data = s.recv(1024).decode()
        server_name, server_int = data.split(",")
        server_int = int(server_int)
        print(f"Client Name: {CLIENT_NAME}")
        print(f"Server Name: {server_name}")
        print(f"Client Integer: {CLIENT_INT}")
        print(f"Server Integer: {server_int}")
        print(f"Sum: {CLIENT_INT + server_int}")
