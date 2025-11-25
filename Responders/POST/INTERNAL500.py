class Responded_INTERNAL:
    __THE500PAGE = '/Users/Racem/Desktop/ExposeWeb/Example_HTML/Permissions&BlockedList/500.html'
    __FILENAME = '/Users/Racem/Desktop/ExposeWeb/MiniServer/Responses/500INTERNAL.txt'

    def __init__(self, max):
        self.__MAXAGE = max
        self.__Response = ''
        self.__Response2 = ''
        self.__contentLength = 0

        with open(self.__FILENAME, 'r') as file:
            for line in file:
                self.__Response += line

        self.__Response += f'max-age: {self.__MAXAGE}'
        self.__contentLength += len(self.__Response)

        # Body:
        with open(self.__THE500PAGE, 'r') as file:
            for line in file:
                self.__contentLength += len(line)
                self.__Response2 += line

        __FIXED = f'\n\rContent-Length: '
        self.__Response += __FIXED + str(self.__contentLength + len(__FIXED) + 4) + '\n\r\n\r' + self.__Response2

    def getResponse(self):
        return self.__Response
