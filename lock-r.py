#creates class that generates new instance of a user

class User:

    user_list = []


    #method that takes properties of user
    def __init__(self, username, password):

         self.username = username
         self.password = password


    #method that saves new user instance to user_list
    def save_user(self):

        User.user_list.append(self)   


    #decorator that displays user list
    @classmethod
    def display_user(cls):
        return cls.user_list


    #method that deletes saved account
    def delete_user(self):

        User.user_list.remove(self)    



#class that creates new instance of credentials

class Credentials():

    credentials_list = []


    #method to verify whether user is in users_list
    @classmethod
    def verify_user(cls,username, password):

        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user
    

    #method that defines attributes of user credentials to be saved
    def __init__(self,account,userName, password):

        self.account = account
        self.userName = userName
        self.password = password


    #method to store new credential to credential list
    def save_details(self):

        Credentials.credentials_list.append(self)


    #