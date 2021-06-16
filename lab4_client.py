# Import all needed libraries
import socket
import time
import json

# Setting the host and port settings.
HOST = '127.0.0.1'
PORT = 3000

# Creating the socket and connecting to the host.
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

shopName = "AllTrend"
cart = []
clothesInCart = False
shoesInCart = False


def clothesMenu():
    ''' The clothes menu function '''
    global cart
    choice = 0
    # Setting up the clothes in the store.
    clothes = {
        "1": "Black Top Nike Men ",
        "2": "Grey Top Nike Men",
        "3": "Yellow Top Nike Men",
        "4": "Blue Top Nike Men",
        "5": "Black Top Nike Women",
        "6": "Yellow Top Nike Women",
        "7": "Blue Top Nike Women",

    }
    # Printing out all the clothes in the store.
    print("This is the clothes menu: ")
    for key in clothes:
        print(key + ":" + clothes[key])
    # Choosing clothes from the store.
    while True:
        choice = input("What would you like to have? ")
        if "done" in choice.lower():
            break
        else:
            cart.append(clothes[choice])
    global clothesInCart
    clothesInCart = True
    if shoesInCart == False:
        shoesChoice = input("Would you like to buy some shoes maybe? ")
        if "yes" in shoesChoice.lower():
            shoesMenu()
        else:
            print("Your order is: ")
            for item in cart:
                print("A " + item)
            print("Thank you and have a nice day!")
    print("Your order is: ")
    for item in cart:
        print("A " + item)
    print("Thank you and have a nice day!")


def shoesMenu():
    ''' The shoes menu function '''
    global cart
    choice = 0
    # Setting up the shoes in the store.
    shoes = {
        "1": "Converse",
        "2": "Nike Air",
        "3": "Nike Jordans",
        "4": "Nike ZoomX",
        "5": "Nike Blazer",

    }
    # Printing out all the shoes in the store.
    print("This is the shoes menu: ")
    for key in shoes:
        print(key + ":" + shoes[key])
    # Choosing shoes from the store.
    while True:
        choice = input("What would you like to have? ")
        if "done" in choice.lower():
            break
        else:
            cart.append(shoes[choice])
    global shoesInCart
    shoesInCart = True
    if clothesInCart == False:
        clothesChoice = input("Would you like to buy some clothes too? ")
        if "yes" in clothesChoice.lower():
            clothesMenu()
        else:
            print("Your order is: ")
            for item in cart:
                print("A " + item)
    print("Your order is: ")
    for item in cart:
        print("A " + item)
    print("Thank you and have a nice day!")

# Log in to the store.
print("Welcome at " + shopName + " !")
print("Could you tell me your name please?")
userName = input()
print("Greetings " + userName)
time.sleep(1)
# Making the order.
orderType = input(
    "We have two sections for you, first section is all about clothes, and the other section is a collection of shoes.\n What would you like to buy today? "
)
orderType = orderType.lower()
if "clothes" in orderType:
    clothesMenu()
elif "shoes" in orderType or "shoe" in orderType:
    shoesMenu()
# Sending the order to the server.
data = {"userName": userName, "cart": cart}
data = json.dumps(data)
data = data.encode()
socket.send(data)

# Closing the socket.
socket.close()