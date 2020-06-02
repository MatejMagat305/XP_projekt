
import unittest
import sys
from io import StringIO

from fake_menu_waitress import fake_menu_waitress
from fake_menu_cook import fake_menu_cook
from fake_menu_admin import fake_menu_admin
from menu import menu

w = "ahoj z fake_menu_waitress\n"
c = "ahoj z fake_menu_cook\n"
a = "ahoj z fake_menu_admin\n"
exit0 = "system sa zatvára\n"
standart = """vytaj v systeme
ak chceš vojsť do menu pre časníkov zadaj: 1
ak chceš vojsť do menu pre kuhárov zadaj: 2
ak chceš vojsť do menu pre admina zadaj: 3
ak chceš ukončiť program zadaj: 4
"""
error = "chyba nepoznám príkaz\n"
bad_input = "nezadal si číslo! skúš ešte raz\n"

class TestStringMethods(unittest.TestCase):
    values = [
        (standart+exit0) ,
        (standart+w+standart+exit0),
        (standart+c+standart+exit0),
        (standart+a+standart+exit0),
        (standart+bad_input+exit0),
        (standart+error+standart+exit0)
        ]
        
    def init_menu(self):
        goal = menu()
        goal.w = fake_menu_waitress()
        goal.c = fake_menu_cook()
        goal.a = fake_menu_admin()
        return goal
    
    def set_std(self, input0):
        sys.stdin =  StringIO(input0)
        sys.stdout = StringIO()

    def unset(self):
        sys.stdin = sys.__stdin__
        sys.stdout= sys.__stdout__

    def test_4(self):
        self.set_std("4")
        self.init_menu().start()
        self.assertEqual(sys.stdout.getvalue(), self.values[0])
        self.unset()
    
    def test_1(self):
        self.set_std("1\n4")
        self.init_menu().start()
        self.assertEqual(sys.stdout.getvalue(), self.values[1])
        self.unset()

    def test_2(self):
        self.set_std("2\n4")
        self.init_menu().start()
        self.assertEqual(sys.stdout.getvalue(), self.values[2])
        self.unset()

    def test_3(self):
        self.set_std("3\n4")
        self.init_menu().start()
        self.assertEqual(sys.stdout.getvalue(), self.values[3])
        self.unset()
    
    def test_No_Number(self):
        self.set_std("jmnk\n4")
        self.init_menu().start()
        self.assertEqual(sys.stdout.getvalue(), self.values[4])
        self.unset()

    def test_5(self):
        self.set_std("5\n4")
        self.init_menu().start()
        self.assertEqual(sys.stdout.getvalue(), self.values[5])
        self.unset()

if __name__ == '__main__':
    unittest.main()
