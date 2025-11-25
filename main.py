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
    global Response, clientNumber

    request = connection.recv(1024).decode('utf-8')
    print(request)

    requestType = re.search(r"^[A-Z]+", request)

    if not requestType:
        connection.close()
        return

    requestType = requestType.group()

    # Extract path
    link = re.search(r"\s\/[^\s]*", request)
    if not link:
        connection.close()
        return

    link = baseUrl + link.group()[1:]

    # HEAD behaves like GET but WITHOUT body
    sendBody = True
    if requestType == "HEAD":
        sendBody = False

    role = hasRole()
    Sender = ChooseAndSend(requestType, link, sendBody, 1)
    Response = Sender.getResponse()

    print(Response)
    connection.sendall(Response.encode('utf-8'))
    connection.close()


while True:
    connection, address = server.accept()
    myThread = threading.Thread(target=userThread, args=([connection]))
    clientNumber += 1
    myThread.start()
