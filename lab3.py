# Import requests and urllib for sending requests.
import requests
import urllib

# Settign up the proxy dictionary
proxyDict = {
              "http"  : "http://me.utm.md:80",
            }

# Creating the menu and the infinite loop.
while True:
    print("Choose the type of request that you would like to make:")
    print("1. GET")
    print('2. POST')
    print('3. HEAD')
    print('4. OPTIONS')
    choose = int(input())

    # Sending the GET request.
    if choose == 1:
        url = input("Introduce the link to acces:")
        r = requests.get(url, proxies=proxyDict)
        print(r.content)
    # Sending the POST request.
    elif choose == 2:
        url = input("Introduce the link to acces:")
        context = input("Introduce message to send:")
        r = requests.post(url, data={'data' : context}, proxies=proxyDict)
        print(r.content)
    # Sending the HEAD request.
    elif choose == 3:
        url = input("Introduce the link to acces:")
        r = requests.head(url, proxies=proxyDict)
        print(r.content)
    # Sending the OPTIONS sequest.
    elif choose == 4:
        url = input("Introduce the link to acces:")
        r = requests.options(url, proxies=proxyDict)
        print(r.content)
    # Breaking up the infinite loop.
    elif choose == 0:
        break
    else:
        print('No such option, try again!')