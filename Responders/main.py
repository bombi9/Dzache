from .GET.Choose import Choose_Response_GET
# Assuming you will create a HEAD response handler
from .HEAD.Choose import Choose_Response_HEAD  

class ChooseAndSend:
    _MaxAge = 90000

    def __init__(self, requestTyp, requestlnk, rle, usrcnt):
        global getResponse

        self._requestType = requestTyp
        self.__requestLink = requestlnk
        self._role = rle
        self._userCount = usrcnt
        self.serverResponse = ''

        if self._requestType.upper() == "GET":
            response = Choose_Response_GET(
                maxage=ChooseAndSend._MaxAge,
                requestlnk=self.__requestLink,
                rl=self._role,
                uc=self._userCount
            )
            self.serverResponse = response.getResponse()
        
        elif self._requestType.upper() == "POST":
            response = Choose_Response_POST(
                maxage=ChooseAndSend._MaxAge,
                requestlnk=self.__requestLink,
                rl=self._role,
                uc=self._userCount
            )
            self.serverResponse = response.getResponse()
        
        elif self._requestType.upper() == "HEAD":
            response = Choose_Response_HEAD(
                maxage=ChooseAndSend._MaxAge,
                requestlnk=self.__requestLink,
                rl=self._role,
                uc=self._userCount
            )
            # For HEAD, you might only want headers
            self.serverResponse = response.getHeaders()
        elif self._requestType.upper() == "UPDATE":
            pass
        elif self._requestType.upper() == "DELETE":
            pass
        else:
            pass

    def getResponse(self):
        return self.serverResponse
