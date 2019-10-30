'''
'''
import unittest

from gen import frange

class TestGen(unittest.TestCase):

    def test(self):
        self.assertEqual(list(frange(1.1, 3)), [1.1, 1.35, 1.6, 1.85, 2.1, 2.35, 2.6, 2.85])
        self.assertEqual(list(frange(3, 1)), [])
        self.assertEqual(list(frange(1, 3, 0)), [])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()