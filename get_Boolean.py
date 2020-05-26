
from get_string import get_string

class get_Boolean:
    def get(self, co:str) -> bool:
        while True:
            answer = get_string().get_one_string(co + " ak ano zadaj: Y, ak nie zadaj: N\n").upper()
            if answer == "Y":
                return True
            elif answer == "N":
                return False
            else:
                print("opakuj")

