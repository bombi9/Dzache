import socket
import re
import threading
from Responders.main import ChooseAndSend

baseUrl = '/Users/Racem/Desktop/ExposeWeb/Example_HTML'
ip = socket.gethostbyname(socket.gethostname())
port = 6767

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen()
Response = ''
clientNumber = 0

def hasRole():
    return True

def userThread(connection):
    message = connection.recv(8192).decode('utf-8', errors='ignore')
    print(message)

    requested = re.compile(r'GET\s+/[a-zA-Z0-9\./]*')
    link = requested.match(message)

    print("Requested:", link.group()[4:])

    requestType = link.group()[:3]
    link = baseUrl + link.group()[4:]
    role = hasRole()

    Sender = ChooseAndSend(requestType, link, True, 1)
    Response = Sender.getResponse()

    print(Response)
    connection.sendall(Response.encode('utf-8'))
    connection.close()

while True:
    connection, address = server.accept()
    myThread = threading.Thread(target=userThread, args=([connection]))
    clientNumber += 1
    myThread.start()