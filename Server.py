import socket

# Connecting to the client

def connection():
    global host
    global port
    global s

    # Host IP is yet to find
    host = ''
    port = 9090

    s = socket.socket()
    s.bind((host, port))
    s.listen(10)
    print ("looking for users")

    global conn1
    global addr1
    conn1 , addr1 = s.accept()



# Verifying users LogIn Data

def users_list():

    # Check the option selected
    # Use signing_up function if signing up
    # Use code below if signing in

    login_input = socket.socket
    users_login_input = login_input.recv(1024)
    user_login = users_login_input.decode(str = 'utf-8' , error = 'strict')
    file = open( 'users_info.txt' , 'a')
    users_data = file.readline()

    # Make a loop to try again and again (not if else)

    if users_login in users_data:

        # Use signing_in function here
        print ("welcome")
    else:
        print ("Login ID or Password is incorrect")
    file.close()

    global user_login_info
    user_login_info = user_login
    return user_login_info


# User signing up


def signing_up():

    file = open('users_info.txt' , 'a')
    file.write(user_login_info)
    file.close()

    user_file = open('username.txt' , 'a')

    # Make a Thread
    # Close the user_file


def signing_in():












