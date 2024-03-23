import json
import re

def valid_username():
    user_name=input("Username :")
    valid=r'[a-zA-Z_][a-zA-Z0-9_]{4,}$'
    if re.match(valid,user_name):
        return user_name
    else:
        print("Invalid username\nEnter valid username")
        valid_username()

def valid_password():
    password=input("Password :")
    valid=r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*()_+}{":;\'?/>.<,])(?=.{8,})'
    if re.match(valid,password):
        return password
    else:
        print("Invalid password\nEnter valid password")
        valid_password()

def valid_email():
    email=input("Email :")
    valid=r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(valid,email):
        return email
    else:
        print("Invalid email\nEnter valid email")
        valid_email()

# To add user who can see the secret file

def add_user():
    main_key='123@'
    key=input("Enter the key :")
    if key==main_key:
        user_name=valid_username()
        password=valid_password()
        email=valid_email()
        data={"username":user_name,"password":password,"email":email}
        with open("credentials_data.json","w") as file:
            json.dump(data,file)

# Check if the user is authenticated or not
def auth():
    user_name=valid_username()
    password=valid_password()
    email=valid_email()
    with open("credentials_data.json","r") as file:
        data=json.load(file)
        if user_name==data["username"] and password==data["password"] and email==data["email"]:
            with open('secret_file.txt','r') as file:
                print(file.read())
        else:
            print("User is not authenticated")

#add_user()
auth()