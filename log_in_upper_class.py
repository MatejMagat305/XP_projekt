from Conection_database import connection
from TestExceptions import NotLogIn

class log_in:
    def __init__(self, fileTxt):
        with open(fileTxt, "r") as file:
            self.scipt_log_in = file.read()

    def log_in(self):
        name, password = get_string().get_string_and_sifr(apply_name, apply_password)
        id0 = connection.executeQuery(self.scipt_log_in, name, password)
        if id0!=None:
            print("ste prihlaseny")
            return id0[0]
        raise NotLogIn("nie je taky")
