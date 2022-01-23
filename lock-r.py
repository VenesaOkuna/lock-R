import random
import string
import pyperclip

#creates class that generates new instance of a user
class User:

    user_list = []


    #function that takes properties of user
    def __init__(self, username, password):

         self.username = username
         self.password = password


    #function that saves new user instance to user_list
    def save_user(self):

        User.user_list.append(self)   


    #method that displays user list
    @classmethod
    def display_user(cls):
        return cls.user_list


    #function that deletes saved account
    def delete_user(self):

        User.user_list.remove(self)    



#class that creates new instance of credentials

class Credentials():

    credentials_list = []


    #function to verify whether user is in users_list
    @classmethod
    def verify_user(cls,username, password):

        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user
    

    #function that defines attributes of user credentials to be saved
    def __init__(self,account,userName, password):

        self.account = account
        self.userName = userName
        self.password = password


    #function to store new credential to credential list
    def save_details(self):

        Credentials.credentials_list.append(self)


    #function to delete credentials
    def delete_credentials(self):

        Credentials.credentials_list.remove(self)


    #Function to search credentials using application name
    @classmethod
    def find_credential(cls, account):

        for credential in cls.credentials_list:
            if credential.account == account:
                return credential


    #copy password to clipboard using pyperclip
    @classmethod
    def copy_password(cls,account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)


    #function that checks if user credentials exist
    @classmethod
    def if_credential_exist(cls, account):

        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    #function that returns all saved passwords
    @classmethod
    def display_credentials(cls):

        return cls.credentials_list