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


    #clean up after each test case has run
    def tearDown(self):

        Credentials.credentials_list = []


    #test saving multiple credentials
    def test_save_many_accounts(self):

        self.new_credential.save_details()
        test_credential = Credentials("IG","Nessa","flipn890") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)


    #test delete credentials
    def test_delete_credential(self):

        self.new_credential.save_details()
        test_credential = Credentials("IG","Nessa","flipn890")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)


    #test to find credential by application name
    def test_find_credentialr(self):

        self.new_credential.save_details()
        test_credential = Credentials("IG","Nessa","flipn890") 
        test_credential.save_details()

        the_credential = Credentials.find_credential("IG")

        self.assertEqual(the_credential.account,test_credential.account)


    #test to get boolean value whether we can find credential
    def test_credential_exist(self):

        self.new_credential.save_details()
        the_credential = Credentials("IG", "Nessa", "flipn890")  
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("IG")
        self.assertTrue(credential_is_found) 

    #test display credentials
    def test_display_all_saved_credentials(self):


        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == "__main__":
    unittest.main()