def TEST(first, second, chyba):
    if isinstance(second, Exception) and first != second.getMessage():
        raise Exception
    if first != second:
        raise Exception(chyba)

class FileNotFound(Exception):
    def __init__(self, message):
        self.message = message
    def getMessage(self):
        return self.message


class ConnectionError(Exception):
    def __init__(self, mesange):
        self.mesange = mesange

    def getMesenge(self):
        return self.mesange