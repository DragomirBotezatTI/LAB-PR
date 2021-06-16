# importing all needed labraries.
import socket
import json

# setting up the HOST and the PORT.
HOST = '127.0.0.1'
PORT = 3000

# Creating and setting up the socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

# Setting up the socket into the accepting mode.
data, address = sock.recvfrom(1024)
print("A connection with " + str(address[0]) + " was made.")

# Decoding and loading the content from the client.
data = data.decode('utf-8')
data = json.loads(data)

# Showing the users order.
showedItems = []
print(data["userName"] + "'s order is: ")
for item in data["cart"]:
    if item not in showedItems:
        showedItems.append(item)
        print(item + " x" + str(data["cart"].count(item)))
    else:
        continue
# Closing the connection and the socket.
sock.close()