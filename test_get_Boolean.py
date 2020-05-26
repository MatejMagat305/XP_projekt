
import unittest
import sys
from io import StringIO
from get_Boolean import get_Boolean



class TestStringMethods(unittest.TestCase):

    def test_YES(self):
        temp = sys.stdin
        sys.stdin = StringIO('Y')
        self.assertEqual(get_Boolean().get("test"), True)
        sys.stdin = temp
        print()

    def test_NO(self):
        temp = sys.stdin
        sys.stdin = StringIO('N')
        self.assertEqual(get_Boolean().get("test"), False)
        sys.stdin = temp
        print()
        
    def test_yes(self):
        temp = sys.stdin
        sys.stdin = StringIO('y')
        self.assertEqual(get_Boolean().get("test"), True)
        sys.stdin = temp
        print()

    def test_no(self):
        temp = sys.stdin
        sys.stdin = StringIO('n')
        self.assertEqual(get_Boolean().get("test"), False)
        sys.stdin = temp
        print()

if __name__ == '__main__':
    unittest.main()
