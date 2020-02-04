USER_NAME = input("Input your name: ")
USER_PASSWORD = input("Input your password: ")

VALID_PASSWORD = "qwe123"

while True:
    if USER_PASSWORD == VALID_PASSWORD:
        print("Password for user: {} is correct".format(USER_NAME))
        break
    else:
        print("Password for user: {} is incorrect".format(USER_NAME))
        print("Please try again...")
        USER_PASSWORD = input("Input your password: ")
