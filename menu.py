from menu_waitress import menu_waitress
from menu_cook import menu_cook
from menu_admin import menu_admin


class menu:
    waitress_menu = 1
    cook_menu = 2
    admin_menu = 3
    finish_menu = 4
    error = "chyba nepoznám príkaz"
    welcome = "vytaj v systeme"
    wiatress = "ak chceš vojsť do menu pre časníkov zadaj: {}"
    cook = "ak chceš vojsť do menu pre kuhárov zadaj: {}"
    admin = "ak chceš vojsť do menu pre admina zadaj: {}"
    finish = "ak chceš ukončiť program zadaj: {}"
    bad_input = "nezadal si číslo! skúš ešte raz"
    exit0 = "system sa zatvára"
    def __init__(self):
        self.w = menu_waitress()
        self.c = menu_cook()
        self.a = menu_admin()
    def start(self):
        while True:
            self.print_menu()
            answer = self.get_answer()
            if answer == self.waitress_menu:
                self.w.start()
            elif answer == self.cook_menu:
                self.c.start()
            elif answer == self.admin_menu:
                self.a.start()
            elif answer == self.finish_menu:
                print(self.exit0)
                break
            else:
                print(self.error)

    def get_answer(self):
        while True:
            try:
                return int(input())
            except ValueError:
                print(self.bad_input)


    def print_menu(self):
        print(self.welcome)
        print(self.wiatress.format(self.waitress_menu))
        print(self.cook.format(self.cook_menu))
        print(self.admin.format(self.admin_menu))
        print(self.finish.format(self.finish_menu))
        


if __name__ == '__main__':
    menu().start()
