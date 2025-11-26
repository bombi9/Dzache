class Choose_Response_PUT:
    def __init__(self, maxage, requestlnk, rl, uc, message):
        self.message = message
        self.file_path = self._extract_path(requestlnk)

    def _extract_path(self, link):
        return os.path.join(BASE, link.lstrip("/"))

    def getResponse(self):
        body = self.message.split("\r\n\r\n", 1)[1] if "\r\n\r\n" in self.message else ""

        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(body)

        return (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            "Dzache/1.0.0: OK\r\n"
            "Connection: close\r\n\r\n"
            "File saved."
        )
