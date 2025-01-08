#validate user input exercise
# 1. Username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


username = input("Enter a username: ")

if len(username) > 12:
    print("This username is not valid")
elif not username.find(" ") == -1:
    print("This username is not valid")
elif not username.isalpha():
    print("This username is no valid")
else:
    print(f"This username is valid, hello {username}")