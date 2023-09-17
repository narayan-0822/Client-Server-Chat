import socket

# Connecting to the server

def connection():
    global s
    global host
    global port
    global username

    host = ''
    port = 9090

    s = socket.socket()
    s.connect((host , port))
    print ("connecttion established")

    # Ask either to login or sign up
    # Send the option selected
    # Use input function in both cases

    def input():
        username = input("Enter your Username - ")
        password = input("\nEnter your Password - ")
        info = str(username) + str(password)
        s.send(info)





