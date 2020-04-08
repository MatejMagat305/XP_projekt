
class MyError(Exception):
    def __init__(self, mesange):
        self.mesange = mesange

    def getMesenge(self):
        return self.mesange
        
