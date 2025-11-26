class Choose_Response_DELETE:
    def __init__(self, maxage, requestlnk, rl, uc, message):
        self.file_path = os.path.join(BASE, requestlnk.lstrip("/"))

    def getResponse(self):
        if not os.path.exists(self.file_path):
            return (
                "HTTP/1.1 404 Not Found\r\n"
                "Content-Type: text/plain\r\n\r\n"
                "File not found."
            )

        os.remove(self.file_path)
        return (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n\r\n"
            "File deleted."
        )
