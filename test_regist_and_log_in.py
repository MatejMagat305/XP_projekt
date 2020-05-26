

import unittest
from registration import registration
from log_cook import log_cook
from io import StringIO
import sys
from coding import coding
from fake_Connection_database import fake_Conection_database
R = registration()
LK=log_cook()
class TestStringMethods(unittest.TestCase):

    def test_regist_kuchar(self):
        sys.stdout= StringIO()
        meno,heslo = "Matej","543210"
        sys.stdin = StringIO(meno+'\n'+heslo)
        R.connection = fake_Conection_database()
        R.connection.good_sql_exe_script="\ninsert into xpkuchari( meno, heslo) VALUES (%s,%s)"
        R.regist_cook()
        self.assertEqual(sys.stdout.getvalue(), "registracia kuchara\nzadaj meno:\nzadaj heslo:\npodarilo sa\n")
        self.assertEqual(list(R.connection.values.keys())[0], tuple([meno, coding().hash_password(heslo)]))
        sys.stdin = sys.__stdin__
        sys.stdout= sys.__stdout__


    def test_regist_casnik(self):
        sys.stdout= StringIO()
        meno,heslo = "Matej","543210"
        sys.stdin = StringIO(meno+'\n'+heslo)
        R.connection = fake_Conection_database()
        R.connection.good_sql_exe_script="\ninsert into xpcasnici( meno, heslo) VALUES (%s,%s)"
        R.regist_waiter()
        self.assertEqual(sys.stdout.getvalue(), "registracia casnika\nzadaj meno:\nzadaj heslo:\npodarilo sa\n")
        self.assertEqual(list(R.connection.values.keys())[0], tuple([meno, coding().hash_password(heslo)]))
        sys.stdin = sys.__stdin__
        sys.stdout= sys.__stdout__

    def test_regist_kuchar(self):
        i = 1
        try:
            sys.stdout= StringIO()
            meno,heslo = "Matej","543210"
            sys.stdin = StringIO(meno+'\n'+heslo)
            R.connection = fake_Conection_database()
            R.connection.good_sql_exe_script="\ninsert into xpkchari( meno, heslo) VALUES (%s,%s)"
            R.regist_cook()
        except:
            i=0
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout= sys.__stdout__

        self.assertEqual(i,0)


    def test_regist_casnik(self):
        i = 1
        try:
            sys.stdout= StringIO()
            meno,heslo = "Matej","543210"
            sys.stdin = StringIO(meno+'\n'+heslo)
            R.connection = fake_Conection_database()
            R.connection.good_sql_exe_script="\ninsert into xpcsnici( meno, heslo) VALUES (%s,%s)"
            R.regist_waiter()
        except:
            i=0
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout= sys.__stdout__
        self.assertEqual(i,0)

    def test_log_in_casnik(self):
        meno,heslo = "Matej","543210"
        sys.stdin = StringIO(meno+'\n'+heslo)
        R.connection = fake_Conection_database()
        R.connection.good_sql_exe_script="\ninsert into xpcasnici( meno, heslo) VALUES (%s,%s)"
        R.regist_waiter()        
        sys.stdout= StringIO()
        sys.stdin = StringIO('y\n'+meno+'\n'+heslo)        
        LK.connection =  R.connection
        LK.connection.good_sql_query_script ="\nselect id from xpcasnici where meno= %s and heslo= ''|| %s"
        self.assertEqual(LK.log_in(),1)
        self.assertEqual(sys.stdout.getvalue(), "naozaj sa chces prihlásiť ako časník? ak ano zadaj: Y, ak nie zadaj: N\nzadaj meno:zadaj heslo:ste prihlaseny\n")
        sys.stdin = sys.__stdin__
        sys.stdout= sys.__stdout__

if __name__ == '__main__':
    unittest.main()
