import unittest
import helloworld

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        pass
        
    def tearDown(self):
        pass


    def testStr(self):
        self.assertEquals(helloworld.getHelloWorld(), "Hello World!")
