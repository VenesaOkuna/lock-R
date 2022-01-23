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


#login user function
def login_user(username,password):

  
    check_user = Credentials.verify_user(username,password)
    return check_user


#create new credential function
def create_new_credential(account,userName,password):

    new_credential = Credentials(account,userName,password)
    return new_credential


#save new credentials function
def save_credentials(credentials):

    credentials. save_details()


#display all saved credentials function
def display_accounts_details():

    return Credentials.display_credentials()


#delete credentials function
def delete_credential(credentials):

    credentials.delete_credentials()


#find credentials by account name function
def find_credential(account):

    return Credentials.find_credential(account)


#check if credential exists using account name
def check_credendtials(account):

    return Credentials.if_credential_exist(account)


#generate random password function
def generate_Password():

    auto_password=Credentials.generatePassword()
    return auto_password


#copy password to clipboard using paperclip framework to copy email function
def copy_password(account):

    return Credentials.copy_password(account)