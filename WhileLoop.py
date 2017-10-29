savedpassword='python123'
password=''
while password != savedpassword:
    password=input("Enter password: ")
    if password == savedpassword:
        print("You are logged in")
    else:
        print("Sorry try again")
