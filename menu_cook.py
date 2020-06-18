
from get_answer import get_answer
from log_cook import log_cook
from registration import registration
from TestExceptions import NotLogIn

class menu_cook:
    cook_id = None
    exit_code = 1
    finish = "ak chceš ukončiť program zadaj: {}"
    log_in_masange = "ak sa chceš prihlasit zadaj {}, alebo registrovat {}"
    log_out_masange="tvoje id je {}, ak sa ches odhlasit zadaj: {}, ale ako prihlaseny môzes tieto veci:"
    log_in_num, regist_num, log_out_num = 2,3,4

    def try_log_in(self):
        try:
            self.cook_id = log_cook().log_in()
        except NotLogIn as e:
            print(e.getMesenge())
            self.cook_id = None 

    def print_log_in(self):
        print("undefine")
    
    def print(self):
        if self.cook_id == None:
            print(self.log_in_masange.format(self.log_in_num, self.regist_num))
        else:
            print(self.log_out_masange.format(self.cook_id, self.log_out_num))
            self.print_log_in()
        print(self.finish.format(self.exit_code))

    def extend_menu(self,answer):
        print("undefine")
        
    def start(self):
        while True:
            self.print()
            answer = get_answer().get()
            if answer == self.exit_code:
                break
            elif answer == self.regist_num:
                registration().regist_cook()
            elif answer == self.log_in_num:
               self.try_log_in()
            elif answer == self.log_out_num:
                self.cook_id = None
            elif self.cook_id != None and answer<10:
                self.extend_menu(answer)
            else:
                print("chyba nepoznám príkaz")
            




