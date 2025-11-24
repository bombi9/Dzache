class Responded_INTERNAL:
    __THE403PAGE = '/Users/Racem/Desktop/ExposeWeb/Example_HTML/Permissions&BlockedList/500.html'
    __FILENAME = '/Users/Racem/Desktop/ExposeWeb/MiniServer/Responses/500INTERNAL.txt'
    __Response, __Response2, __contentLength, __MAXAGE = '', '', 0, 0

    def getResponse(self):
        return self.__Response
    
    def __init__(self, max):
        self.__MAXAGE = max

    with open(__FILENAME, 'r') as file:
        for line in file:
            __Response += line
    __Response += f'max-age: {__MAXAGE}'
    __contentLength += len(__Response)

    # Body:
    with open(__THE403PAGE, 'r') as file:
        for line in file:
            __contentLength += len(line)
            __Response2 += line
    __FIXED = f'\n\rContent-Length: '
    __Response += __FIXED + str(__contentLength+len(__FIXED)+4) + '\n\r\n\r' + __Response2