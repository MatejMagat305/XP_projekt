
import unittest
import sys
from io import StringIO
from get_Boolean import get_Boolean



class TestStringMethods(unittest.TestCase):

    def test_YES(self):
        sys.stdin = StringIO('Y')
        self.assertEqual(get_Boolean().get("test"), True)
        sys.stdin = sys.__stdin__
        print()

    def test_NO(self):
        sys.stdin = StringIO('N')
        self.assertEqual(get_Boolean().get("test"), False)
        sys.stdin = sys.__stdin__
        print()
        
    def test_yes(self):
        sys.stdin = StringIO('y')
        self.assertEqual(get_Boolean().get("test"), True)
        sys.stdin = sys.__stdin__
        print()

    def test_no(self):
        sys.stdin = StringIO('n')
        self.assertEqual(get_Boolean().get("test"), False)
        sys.stdin = sys.__stdin__
        print()

if __name__ == '__main__':
    unittest.main()
