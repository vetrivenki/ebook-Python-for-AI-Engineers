saved_username = "admin"
saved_password = "python123"

username = input("Username: ")
password = input("Password: ")

if username == saved_username and password == saved_password:
    print("Login successful")
elif username != saved_username:
    print("Unknown username")
else:
    print("Incorrect password")
