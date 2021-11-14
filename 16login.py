def logIn(UID="Admin", Pass="St0rE@1"):
    i = 0
    while i < 3:
        uid = input("Enter the User ID: ")
        password = input("Enter The Password: ")
        i += 1
        if UID == uid and Pass == password:
            print("Login Successful")
            break
        elif i == 3:
            print("Account Locked")
        else:
            print("Try Again")


logIn()
