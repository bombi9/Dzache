import datetime
import os

class Responded_OK:
    __FILENAME = '/Users/Racem/Desktop/ExposeWeb/MiniServer/Responses/200OK.txt'

    def __init__(self, HName, max):
        self.__MAXAGE = max
        self._htmlLink = HName
        self._Response = ""
        dotIndex= self._htmlLink.find('.')
        _contentType = self._htmlLink[dotIndex+1:]

        with open(self.__FILENAME, 'r') as file:
            for line in file:
                self._Response += line.rstrip('\n').rstrip('\r') + "\r\n"

        try:
            with open(self._htmlLink, 'r') as f:
                body = f.read()
        except:
            body = "<h1>Internal Error</h1>"

        content_length = len(body)

        now = datetime.datetime.now()
        stat = os.stat(self._htmlLink)
        lastModified = datetime.datetime.fromtimestamp(stat.st_mtime)

        self._Response += f"Content-Type: text/{_contentType.lower()}; charset=utf-8\r\n"
        self._Response += f"Max-Age: {self.__MAXAGE}\r\n"
        self._Response += f"Last-Modified: {lastModified}\r\n"
        self._Response += f"Date: {now}\r\n"
        self._Response += f"Content-Length: {content_length}\r\n"
        self._Response += "\r\n"  

        self._Response = self._Response + body

    def getResponse(self):
        return self._Response
