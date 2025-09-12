import socket

HOST = "0.0.0.0"
PORT = 5001
SERVER_NAME = "Server of Veda Laxman"
SERVER_INT = 42

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"{SERVER_NAME} listening on {HOST}:{PORT}...")

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024).decode()
        client_name, client_int = data.split(",")
        client_int = int(client_int)

        if not (1 <= client_int <= 100):
            print("Invalid number received. Closing server...")
        else:
            print(f"Client Name: {client_name}")
            print(f"Server Name: {SERVER_NAME}")
            print(f"Client Integer: {client_int}")
            print(f"Server Integer: {SERVER_INT}")
            print(f"Sum: {client_int + SERVER_INT}")
            reply = f"{SERVER_NAME},{SERVER_INT}"
            conn.sendall(reply.encode())
