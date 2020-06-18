
from log_in_upper_class import log_in
from TestExceptions import NotLogIn
from get_Boolean import get_Boolean

class log_cook(log_in):
    def __init__(self):
        log_in.__init__(self,"log_cook.txt")

    def log_in(self):
            if get_Boolean().get("naozaj sa chces prihlásiť ako kuchar?"):
               return log_in.log_in(self)
            return None
        

if __name__ == '__main__':        
    log_cook().log_in()
