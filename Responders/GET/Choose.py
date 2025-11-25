from .ERROR404 import Responded_FoF
from .FORBIDDEN403 import Responded_FORBIDDEN
from .INTERNAL500 import Responded_INTERNAL
from .OK200 import Responded_OK
import os.path as OS

serverResponseMessage = ''

class Choose_Response_GET:
    MAXUSERS = 10

    def __init__(self, maxage, requestlnk, rl, uc):
        global serverResponseMessage
        
        self._requestLink = requestlnk
        self._MAXAGE = maxage
        self._haveRole = rl
        self._userCount = uc

        _isDirr = OS.exists(self._requestLink)
        _isFull = self._userCount >= Choose_Response_GET.MAXUSERS

        if (_isDirr and self._haveRole and not _isFull):
            _serverResponse = Responded_OK(self._requestLink, self._MAXAGE)
            serverResponseMessage = _serverResponse.getResponse()
        elif (_isDirr and not self._haveRole and not _isFull):
            _serverResponse = Responded_FORBIDDEN(self._MAXAGE)
            serverResponseMessage = _serverResponse.getResponse()
        elif _isDirr and self._haveRole and _isFull:
            _serverResponse = Responded_INTERNAL(self._MAXAGE)
            serverResponseMessage = _serverResponse.getResponse()
        elif not _isDirr and self._haveRole and not _isFull:
            _serverResponse = Responded_FoF(self._MAXAGE)
            serverResponseMessage = _serverResponse.getResponse()

    def getResponse(self, sendBody=True):
    try:
        with open(self.link, "rb") as f:
            body = f.read()
        header = "HTTP/1.1 200 OK\r\n"
        header += f"Content-Length: {len(body)}\r\n"
        header += "Connection: close\r\n\r\n"

        if sendBody:
            return header + body.decode(errors="ignore")
        else:
            # HEAD → return headers only
            return header

    except FileNotFoundError:
        from Responders.GET.ERROR404 import get404
        return get404()
