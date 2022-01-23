#creates class that generates new instance of a user

class User:

    user_list = []

    #method that takes properties of user
    def __init__(self, username, password):

         self.username = username
         self.password = password