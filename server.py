import socket  # importing sockets.
import threading  # importing Threading.

HEADER = 64  # this id the number of bytes.
PORT = 9999  # this is the port number.
SERVER = "your ip address "  # this line is to get the ip address of this laptop as a server.

ADDR = (SERVER, PORT)  # this line is mentioning the sserver and the port number in one variable that is addr.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # this line creates a server.

server.bind(ADDR)  # this line binds the ip adress and the port number with the server.

FORMAT = 'utf-8'  # this is the format to decode the msg_lenght to convert into the string.

DISCONNECT_MESSAGE = "!DISCONNECT"  # THIS IS THE MESSAGE FOR THE CLIENT TO DISCONNECT FROM THE SERVER.


def hadle_client(conn, addr):
    '''this is a function to handle the code of the client side.
       it shows the new connection. this function also recieve
       the messages from the client '''

    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:

        msg_lenght = conn.recv(HEADER).decode(
            FORMAT)  # this line is recieving the messages from the client and converting into string format.

        if msg_lenght:
            msg_lenght = int(msg_lenght)  # this line recieves the integers

            msg = conn.recv(msg_lenght).decode(FORMAT)  # this line takes the monverte messages.

            '''this statement of "if" shows that if the user/client has
            typed !DISCONNECT then the user will 'disconnect' from the server.'''

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(
                f"[{addr}] sent:{msg}")  # this line prints the message by the client and also the "addr" that is the "ip address of the client".

    conn.close()  # this line closes the connection.


def start():
    '''this function accepts the client and
       and created a new thread, and also
       shows the active connections'''

    server.listen()  # server starts listioning here.

    print(f"[LISTINING] the server is listioning on {SERVER}")  # this line prints the ip address of the server

    while True:
        conn, addr = server.accept()  # this line accepts the connection and the address/"ip adress" of the user/client.

        thread = threading.Thread(target=hadle_client,
                                  args=(conn, addr))  # this line creates the new thread for the user/client.

        thread.start()  # this line strts the thread.

        print(
            f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1} ")  # this line prints the new connections and the active count of the users.


print("[STARTING] Starting the server...")  # this is just a print statement
start()
