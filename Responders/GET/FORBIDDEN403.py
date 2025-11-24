class Responded_FORBIDDEN:
    __THE403PAGE = '/Users/Racem/Desktop/ExposeWeb/Example_HTML/Permissions&BlockedList/403.html'
    __FILENAME = '/Users/Racem/Desktop/ExposeWeb/MiniServer/Responses/403FORBIDDEN.txt'
    __MAXAGE, __Response, __Response2, __contentLength = 0, '', '', 0

    def getResponse(self):
        return self.__Response

    def __init__(self, max):
        self.__MAXAGE = max

    with open(__FILENAME, 'r') as file:
        for line in file:
            __contentLength += len(line)
            __Response += line

    # Now to body:
    with open(__THE403PAGE, 'r') as file:
        for line in file:
            __contentLength += len(line)
            __Response2 += line

    __FIXED = f'\n\rMax-Age: {__MAXAGE}\n\rContent-Length: '
    __Response += __FIXED + str(__contentLength+len(__FIXED)+4) + '\n\r\n\r' + __Response2
