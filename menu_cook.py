
from get_answer import get_answer
from log_cook import log_cook
from registration import registration

class menu_cook:
    cook_id = None
    exit_code = 1
    log_in_masange = "ak sa chceš prihlasit zadaj {}, alebo registrovat {}"
    log_out_masange="tvoje id je {}, ak sa ches odhlasit zadaj{}, ale ako prihlaseny môzes tieto veci:"
    log_in_num, regist_num, log_out_num = 2,3,4

    def print_log_in(self):
        print("undefine")
    
    def print(self):
        if cook_id == None:
            print(self.log_in_masange.format(self.log_in_num, self.regist_num))
        else:
            print(self.log_out_masange.format(self.cook_id, self.log_out_num))
            self.print_log_in()
        print(my_menu.finish.format(exit_code))

    def extend_menu(self,answer):
        print("undefine")
        
    def start(self):
        while True:
            self.print()
            answer = get_answer().get()
            if answer == exit_code:
                break
            elif answer == regist_num:
                registration().regist_cook()
            elif answer == log_in_num:
               cook_id = log_cook().log_in()
            elif answer == log_out_num:
                cook_id = None
            elif cook_id != None:
                self.extend_menu(answer)
            else:
                print("chyba nepoznám príkaz")
            


