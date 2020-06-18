

from Connection_database import Connection
from get_Boolean import get_Boolean
from get_string import get_string

class registration:
    def __init__(self):
        self.connection= Connection()
        with open("insert_script_waiter.txt", "r") as file:
            self.script_waiter = file.read()

        with open("insert_script_cook.txt", "r") as file:
            self.script_cook = file.read()        
            
    def regist_waiter(self):
        while True:
            try:
                print("registracia casnika")
                self.regist(self.script_waiter)
                print("podarilo sa")
                break
            except:
                if self.finish():
                    break

    def  finish(self):
        return not get_Boolean().get("nepodarilo sa skus este raz alebo odid, "+'skusit znova?')

    def regist_cook(self):
        while True:
            print("registracia kuchara")
            try:
                self.regist(self.script_cook)
                print("podarilo sa")
                break
            except:
                if self.finish():
                    break

    def regist(self, script):
        apply_name, apply_password='zadaj meno:\n',"zadaj heslo:\n"
        name_password = get_string().get_string_and_sifr(apply_name, apply_password)
        self.connection.execute(script, tuple(name_password))       

