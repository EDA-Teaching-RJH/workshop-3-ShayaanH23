user_name = "admin"
user_password = "password123"

def login():
    username = input("Please Enter your username: ")
    password = input("Please Enter your password: ")

    if username == user_name and password == user_password:
        print("Access granted.")
    else:
        print("Acess Denied.")

login()

