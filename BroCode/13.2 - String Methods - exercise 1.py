#   Validate user input exercise
#   1. username is no more than 12 characters
#   2. username must contain spaces
#   3.username must not contain digits

username = input("Enter username: ")

username.find(" ")
username.isalpha()

if len(username) > 12:
    print("Your username can't be more than 12 characters!")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces!")
elif not username.isalpha():
    print("Your username can't contain numbers!!!!")
else:
    print(f"Welcome {username}")