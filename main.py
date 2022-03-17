import socket
import sys

c = socket.socket()
server = ('169.254.242.78', 4444)
# Code to try to connect to the server, if failed, changes the port
try:
    c.connect(server)
except ConnectionError:
    print("Can't connect, trying port 4445.")
    server = ('169.254.242.78', 4445)
    try:
        c.connect(server)
    except ConnectionError:
        print("Can't connect. Port 4444 and 4445 are in use. Try again later.")
        sys.exit()
# Prints the possible options for the user
print("Send the number of the option you want: distance / ledon / ledoff / exit.")

while True:
    # We ask the user to write the command
    message = input("Write the option: ")
    # We encode the message and send it to the server
    c.sendall(message.encode('utf-8'))
    try:
        # Menu to show the user the consequence of the action selected
        if message == "distance":
            data, addr = c.recvfrom(1024)
            data = data.decode('utf-8')
            print("Distance from hc-sr04: " + data + "cms.")
        elif message == "ledon":
            print("Led is on.")
        elif message == "ledoff":
            print("Led is off.")
        elif message == "exit":
            print("System shutting down.")
            break
        else:
            print("Wrong message. Must be: distance / ledon / ledoff / exit")
    except KeyboardInterrupt:
        c.close()
        sys.exit()
