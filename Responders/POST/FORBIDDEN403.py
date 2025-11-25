class Responded_FORBIDDEN:
    __THE403PAGE = '/Users/Racem/Desktop/ExposeWeb/Example_HTML/Permissions&BlockedList/403.html'
    __FILENAME = '/Users/Racem/Desktop/ExposeWeb/MiniServer/Responses/403FORBIDDEN.txt'

    def __init__(self, max):
        self.__MAXAGE = max
        self.__Response = ''
        self.__Response2 = ''
        self.__contentLength = 0

        with open(self.__FILENAME, 'r') as file:
            for line in file:
                self.__contentLength += len(line)
                self.__Response += line

        # Body:
        with open(self.__THE403PAGE, 'r') as file:
            for line in file:
                self.__contentLength += len(line)
                self.__Response2 += line

        __FIXED = f'\n\rMax-Age: {self.__MAXAGE}\n\rContent-Length: '
        self.__Response += __FIXED + str(self.__contentLength + len(__FIXED) + 4) + '\n\r\n\r' + self.__Response2

    def getResponse(self):
        return self.__Response
