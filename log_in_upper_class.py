from Conection_database import Connection
from TestExceptions import NotLogIn
from get_string import get_string

class log_in:
    def __init__(self, fileTxt):
        with open(fileTxt, "r") as file:
            self.connection=Connection()
            self.scipt_log_in = file.read()

    def log_in(self):
        apply_name, apply_password = "zadaj meno:", "zadaj heslo:"
        name, password = get_string().get_string_and_sifr(apply_name, apply_password)
        id0 = self.connection.executeQuery(self.scipt_log_in, tuple([name, password]))
        if id0!=None and len(id0)>0 and id0[0]!=None:
            print("ste prihlaseny")
            return id0[0]
        raise NotLogIn("nie je taky")
