#!/usr/bin/env python3.8
from locker import User, Credentials


#graphics
def graphics():
	print("              ___          ____       ______     _      _               _______                   ")
	print("              |  |       /     \    /   ____|   |  |  /  /              |   _   \                 ")
	print("              |  |      |   --   |  |   |       |  | /  /     _____     |  |_|   |                ")
	print("              |  |      |  |  |  |  |   |       |  |\  \     |_____|    |   _   /                 ")
	print("              |  |_____ |   --   |  |   |____   |  | \  \               |  |  \  \                ")
	print("              |_______|  \______/    \______|   |_ |  \__\              | _|   \__\               ")
print("                                                                                                      ")                                         

graphics()


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



def locker():
    
    #welcome message
    print(" Hello, Welcome to Lock-R, A program built to store user credentials ...\n \n Please enter one of the following to proceed.\n CA ---  Sign in  \n LI ---  Have an account, Log in  \n")
    short_code=input("").lower().strip()

    if short_code == "ca":

        print("Fill in the details below")

        print('*' * 170)
        username = input("User_name: ")
        print('*' * 170)

        while True:
            print(" IP - To input own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()

            if password_Choice == 'ip':
                password = input("Enter Password\n")
                break

            elif password_Choice == 'gp':
                password = generate_Password()
                break

            else:
                print("Wrong password, please try again")

        #to save new user Lock-R account        
        save_user(create_new_user(username,password))
        print("*"*85)
        print(f"Dear {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)
        
    #Log in Lock-R account    
    elif short_code == "li":

        print(" ")
        print("*"*50)
        print("Enter Lock-R Username and Password to Log in:")
        print('*' * 50)
        print(" ")

       #verifying log in
        username = input("Username: ")
        password = input("password: ")
        login = login_user(username,password)

        if login_user == login:
            print(f"Hello {username}.Welcome back to Lock-R!")  
            print('\n')

    while True:
        print("Use these codes:\n CC - New Credential \n VC - Display Credentials \n EC - look for existing credential \n GP - Generate A randomn password \n Del - Delete credential \n EX - Logout \n")
        short_code = input().lower().strip()
        
        #new credentials
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Application name:  (e.g 'Instagram')")
            account = input().lower()
            print("Your Account username")
            userName = input()

            while True:
                print(" TP - To type your own password: \n GP - To let Lock-R generate random Password for you")
                password_Choice = input().lower().strip()

                if password_Choice == 'tp':
                    password = input("Enter Your Own Password \n")
                    break

                elif password_Choice == 'gp':
                    password = generate_Password()
                    break

                else:
                    print("Invalid password please try again")

            #save new credential
            save_credentials(create_new_credential(account,userName,password))
            print('\n') 
            print(f"Account Credential for:  {account} -  UserName:  {userName}  -  Password:  {password}  created and saved succesfully!")
            print('\n')
        

        #display/ view credentials
        elif short_code == "vc":

            if display_accounts_details():
                print("Here's your list of saved Credentials: ")
                 
                print('*' * 35)
                print('_'* 35)

                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 35)
                print('*' * 35)
                
            else:
                print("No existing credentials saved yet...")
       
        

        #look for existing credentials using application name
        elif short_code == "ec":
            print("Enter the Application Name you want to search for")
            search_name = input().lower()

            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)

            else:
                print("That Credential does not exist")
                print('\n')
        

        #delete credentials
        elif short_code == "del":
            print("Enter the Application name of the Credentials you want to delete")
            search_name = input().lower()
            
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your credentials for : {search_credential.account} is successfully deleted!!!")
                print('\n')

            else:
                print(" Credential to be deleted does not exist")
         
        #generate random password
        elif short_code == 'gp':

            password = generate_Password()
            print(f" succesfully generated {password} ")

        #log out of Lock-R account
        elif short_code == 'ex':
            print("Thank you for using Lock-R.. See you next time!")
            break

        else:
            print("Wrong entry! let entry match those in menu")
    
    
if __name__ == '__main__':
    locker()