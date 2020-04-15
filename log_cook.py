
from log_in_upper_class import log_in
from TestExceptions import NotLogIn
from get_string import get_string

class cook_log(log_in):
    def __init__(self):
        super.__init__("log_cook.txt")

    def log_in(self):
        name, password = get_string().get_string_and_sifr(apply_name, apply_password)
        id0=super.log_in()
        
        
