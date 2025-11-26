from .GET.Choose import Choose_Response_GET
# Assuming you will create a HEAD response handler
from .HEAD.Choose import Choose_Response_HEAD
from .HEAD.Choose import Choose_Response_PUT
from .HEAD.Choose import Choose_Response_DELETE


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
            match_put = re.search(r"^PUT\s+(/[\w\.\-]*)", message)
            if match_put:
                link = match_put.group(1)
                file_path = os.path.join(BASE, link[1:])

      
            data = message.split("\r\n\r\n", 1)
            body = data[1] if len(data) > 1 else ""

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(body)

            response = "HTTP/1.1 200 OK\r\n\r\nFile saved."
            connection.send(response.encode("utf-8"))
        elif self._requestType.upper() == "PUT":
            response = Choose_Response_PUT(
                maxage=ChooseAndSend._MaxAge,
                requestlnk=self.__requestLink,
                rl=self._role,
                uc=self._userCount,
                message=self._rawMessage
            )
            self.serverResponse = response.getResponse()

        elif self._requestType.upper() == "DELETE":
            response = Choose_Response_DELETE(
                maxage=ChooseAndSend._MaxAge,
                requestlnk=self.__requestLink,
                rl=self._role,
                uc=self._userCount,
                message=self._rawMessage
            )
            self.serverResponse = response.getResponse()

        else:
            response = "Not, a supported request"

    def getResponse(self):
        return self.serverResponse
