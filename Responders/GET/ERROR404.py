import datetime
import os
class Responded_FoF:
    __ErrorPage = '/Users/Racem/Desktop/ExposeWeb/Example_HTML/Permissions&BlockedList/404.html'
    FILENAME = '/Users/Racem/Desktop/ExposeWeb/MiniServer/Responses/404ERROR.txt'
    Response, __MAXAGE, contentLength = '', 0, 0

    def __init__(self, age):
        self.MAXAGE = age

        with open(self.FILENAME, 'r') as file:
            for line in file:
                self.contentLength += len(line)
                self.Response += line

        stat = os.stat(self.FILENAME)
        dateCreated = datetime.datetime.fromtimestamp(stat.st_birthtime)
        lastModified= datetime.datetime.fromtimestamp(stat.st_mtime)
        self.contentLength += len(str(lastModified))
        self.contentLength += len(str(dateCreated))
        self.Response += f"\n\rMax-Age: {self.__MAXAGE}\n\rLast-Modified: {lastModified}\n\rDate: {dateCreated}\n\rContent-Length: {self.contentLength}\n\r\n\r"

        with open(self.__ErrorPage, 'r') as file:
            for line in file:
                self.contentLength += len(line)
                self.Response += line

    def getResponse(self):
        return self.Response