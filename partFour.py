def login(users):
 while True:
    username = input("Please enter your username")
    password = input("PLease enter a password")

    for u in users:
        if username == u[0]:
            if password == [1]:
                return "Access Granted"
        else:
                return "Access not granted"

    
        

users = [["Shayaan", "Hasan223"], ["Askari", "A223"], ["Naqvi", "hh23"]]

username = login(users)

print(username, )

