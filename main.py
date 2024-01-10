import re

print("Sign up")

# Get user input
name = input("Please enter your name: ")
password = input("Please enter your password: ")

# Password validation
try:
    if not (re.search("[a-z]", password) and
            re.search("[A-Z]", password) and
            re.search("[0-9]", password) and
            re.search("[!@#$%^&*()-_+=<>?]", password)):
        raise ValueError("Invalid password format")
except ValueError as e:
    print(e)
    exit()

print("Sign up successful!")

# Login
name2 = input("Please enter your name: ")
password2 = input("Please enter your password: ")

# Check credentials
if name2 == name and password2 == password:
    print("Access allowed!")
else:
    print("Access denied!")



















