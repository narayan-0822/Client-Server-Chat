import socket

# Client configuration
host = 'localhost'
port = 9090

# Start the client and connect to the server
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("Connected to server")

    while True:
        command = input("Enter command (signup/login): ")
        client.send(command.encode('utf-8'))
        
        if command == "signup" or command == "login":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            client.send(username.encode('utf-8'))
            client.send(password.encode('utf-8'))

        response = client.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

# Start the client
start_client()
