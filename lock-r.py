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