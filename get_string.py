
from coding import coding

class get_string:
    def get_string_and_sifr(self,apply_first, apply_second):
            try:
                name = input(apply_first)
                password = input(apply_second)
                return name, coding().hash_password(password)
            except getpass.GetPassWarning :
                print("nepodarilo sa skus este raz zadat")
                return self.get_name_password()

    def get_one_string(self, apply_string):
        return input(apply_string)
