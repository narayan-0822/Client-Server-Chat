import socket
import threading

# Server configuration
host = 'localhost'
port = 9090

# Start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print("Server listening on port", port)

    while True:
        conn, addr = server.accept()
        print(f"Connection from {addr}")
        threading.Thread(target=handle_client, args=(conn,)).start()

# Handle client connections
def handle_client(conn):
    try:
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received data: {data}")
            process_data(data, conn)
    finally:
        conn.close()

# Process received data
def process_data(data, conn):
    if data == "signup":
        signup(conn)
    elif data == "login":
        login(conn)
    else:
        conn.send("Invalid command".encode('utf-8'))

# Handle user signup
def signup(conn):
    username = conn.recv(1024).decode('utf-8')
    password = conn.recv(1024).decode('utf-8')
    # Add hashing and validation here
    with open('users_info.txt', 'a') as file:
        file.write(f"{username},{password}\n")
    conn.send("Signup successful".encode('utf-8'))

# Handle user login
def login(conn):
    username = conn.recv(1024).decode('utf-8')
    password = conn.recv(1024).decode('utf-8')
    # Add authentication logic here
    with open('users_info.txt', 'r') as file:
        for line in file:
            user, passw = line.strip().split(',')
            if user == username and passw == password:
                conn.send("Login successful".encode('utf-8'))
                return
    conn.send("Invalid username or password".encode('utf-8'))

# Start the server
start_server()
