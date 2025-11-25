from Responders.GET.Choose import ChooseGET

class ChooseAndSend:
    def __init__(self, method, link, sendBody, user):
        self.method = method
        self.link = link
        self.sendBody = sendBody
        self.user = user
        self.response = ""

    def getResponse(self):
        # GET + HEAD share same responders
        if self.method == "GET" or self.method == "HEAD":
            chooser = ChooseGET(self.link, self.user)
            self.response = chooser.getResponse(sendBody=self.sendBody)

        else:
            # default 500 internal if method not supported
            self.response = "HTTP/1.1 500 Internal Server Error\r\n\r\nMethod Not Supported"

        return self.response
