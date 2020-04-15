

from Conection_database import connection
from get_string import get_string

class registration:
    def __init__(self):
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
        print("nepodarilo sa skus este raz")
        again ='skusit znova? Y/N:\n'
        odpoved = get_string().get_one_string(again)
        odpoved = odpoved.upper()
        if odpoved == 'Y':
            return False
        return True

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
        connection.execute(script, tuple(name_password))        

r =registration()
r.regist_waiter()
r.regist_cook()
