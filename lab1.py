# importing socket library for Internet protocols.
import socket
# Importin re for regex expressions
import re
import select
# Importing futures from concurrent to use threads.
from concurrent import futures
# Setting up the target host.
target_host = 'me.utm.md'

def get_imgs(img):
    ''' Function for getting the image'''
    global target_host
    # Senting a GET request to the host to get a certain image.
    s.sendall('GET /{} HTTP/1.1\r\nHOST: {}\r\n\r\n'.format(img, target_host).encode())
    # Colecting the binary format of the image.
    reply = b''
    while select.select([s], [], [], 3)[0]:
        data = s.recv(2048)
        if not data: break
        reply += data
    # Setting up the headers.
    headers = reply.split(b'\r\n\r\n')[0]
    # Getting the image.
    image = reply[len(headers) + 4:]
    # Saving the image on local machine.
    f = open('img/{}'.format(img.split('/')[-1]), 'wb')
    f.write(image)
    f.close()

# Creating the socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Getting the adress information.
socket.getaddrinfo(target_host, 80)
# Connecting to the host.
s.connect((target_host , 80))
# Getting the full content of the website - html code.
s.sendall("GET / HTTP/1.1\r\nHost:{}\r\n\r\n".format(target_host).encode())
result = s.recv(1000000000)

# Extracting images names/locations using regex.
imgs = re.findall("src\=.+[png|jpg|gif]\"", result.decode())
imgs = [img.replace('src=\"', '') for img in imgs]
imgs = [img.replace('\"', '') for img in imgs]

# Setting the max number of workers.
MAX_WORKERS = 4
workers = min(MAX_WORKERS, len(imgs))

# Sending every request as a thread.
with futures.ThreadPoolExecutor(workers) as executor:
    # Creating the to do list.
    to_do = []
    for img in imgs:
        future = executor.submit(get_imgs, img)
        to_do.append(future)
    # Collecting the results.
    for future in futures.as_completed(to_do):
        _ = future.result()