from .ERROR404 import Responded_FoF
from .FORBIDDEN403 import Responded_FORBIDDEN
from .INTERNAL500 import Responded_INTERNAL
from .OK200 import Responded_OK
import os.path as OS

serverResponseMessage = ''

class Choose_Response:
    MAXUSERS = 10

    def __init__(self, method, maxage, requestlnk, rl, uc):
        global serverResponseMessage

        self._method = method.upper()
        self._requestLink = requestlnk
        self._MAXAGE = maxage
        self._haveRole = rl
        self._userCount = uc

        _isDirr = OS.exists(self._requestLink)
        _isFull = self._userCount >= Choose_Response.MAXUSERS

        # Determine the appropriate response class
        if _isDirr and self._haveRole and not _isFull:
            _serverResponse = Responded_OK(self._requestLink, self._MAXAGE)
        elif _isDirr and not self._haveRole and not _isFull:
            _serverResponse = Responded_FORBIDDEN(self._MAXAGE)
        elif _isDirr and self._haveRole and _isFull:
            _serverResponse = Responded_INTERNAL(self._MAXAGE)
        elif not _isDirr and self._haveRole and not _isFull:
            _serverResponse = Responded_FoF(self._MAXAGE)
        else:
            # fallback (just in case)
            _serverResponse = Responded_INTERNAL(self._MAXAGE)

        # If method is HEAD, remove body from the response
        if self._method == "HEAD":
            _serverResponse.removeBody()  # You need to implement removeBody() in each response class

        serverResponseMessage = _serverResponse.getResponse()

    def getResponse(self):
        return serverResponseMessage
