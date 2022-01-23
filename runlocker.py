#!/usr/bin/env python3.8
from locker import User, Credentials


#graphics
def function():
	print("              ___          ____       ______     _      _               _______                   ")
	print("              |  |       /     \    /   ____|   |  |  /  /              |   _   \                 ")
	print("              |  |      |   --   |  |   |       |  | /  /     _____     |  |_|   |                ")
	print("              |  |      |  |  |  |  |   |       |  |\  \     |_____|    |   _   /                 ")
	print("              |  |_____ |   --   |  |   |____   |  | \  \               |  |  \  \                ")
	print("              |_______|  \______/    \______|   |_ |  \__\              | _|   \__\               ")
print("                                                                                                      ")                                         

function()


#create account function
def create_new_user(username,password):

    new_user = User(username,password)
    return new_user


#save account function
def save_user(user):

    user.save_user()


#display user details function
def display_user():

    return User.display_user()