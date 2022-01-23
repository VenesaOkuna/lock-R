import unittest
from locker import User
from locker import Credentials

#test class
class TestClass(unittest.TestCase):
    
    #function that sets up test class
    def setUp(self):

        self.new_user = User('Ness','kokokrim')
    
    #test user account
    def test_init(self):

        self.assertEqual(self.new_user.username,'Ness')
        self.assertEqual(self.new_user.password,'kokokrim')


    # test save user account

    def test_save_user(self):

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

 


#test class for credentials
class TestCredentials(unittest.TestCase):

    def setUp(self):

        self.new_credential = Credentials('Gmail','Ness','kokokrim')
   
    def test_init(self):

        self.assertEqual(self.new_credential.account,'Gmail')
        self.assertEqual(self.new_credential.userName,'Ness')
        self.assertEqual(self.new_credential.password,'kokokrim')


    #test to see if credentials is saved to credential list

    def save_credential_test(self):

        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)