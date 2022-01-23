import unittest
from locker import User
from locker import Credentials

#test class
class TestClass(unittest.TestCase):
    
    #function that sets up test class
    def setUp(self):

        self.new_user = User('Ness','kokokrim')
    
    #test 
    def test_init(self):

        self.assertEqual(self.new_user.username,'Ness')
        self.assertEqual(self.new_user.password,'kokokrim')

