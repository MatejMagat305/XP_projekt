

from Conection_database import connection
import getpass
import hashlib, binascii, os

class registration:
    def __init__(self):
        with open("insert_script_waiter.txt", "r") as file:
            self.script_waiter = file.read()

        with open("insert_script_cook.txt", "r") as file:
            self.script_cook = file.read()        
            
    def regist_waiter(self):
        print("registracia casnika")
        self.regist(self.script_waiter)      

    def regist_cook(self):
        print("registracia kuchara")
        self.regist(self.script_cook)

    def regist(self, script):
        name, password = self.get_name_password()
        try:
            connection.execute_regist(script, name, password)
            print("podarilo sa")
        except:
            print("nepodarilo sa skus este raz")
            self.regist_cook()

    def get_name_password(self):
        try:
            name = input('zadaj meno:\n')
            password = getpass.getpass("zadaj heslo:\n")
            return name, self.hash_password(password)
        except getpass.GetPassWarning :
            print("nepodarilo sa skus este raz zadat")
            return self.get_name_password()
    
    def hash_password(self, password):
        return hashlib.sha224(password.encode()).hexdigest()

r =registration()
r.regist_waiter()
r.regist_cook()
