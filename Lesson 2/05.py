user_name = input("Input your name: ")
user_password = input("Input your password: ")

valid_password = "qwe123"

while True:
    if user_password == valid_password:
        print("Password for user: {} is correct".format(user_name))
        break
    else:
        print("Password for user: {} is incorrect".format(user_name))
        print("Please try again...")
        user_password = input("Input your password: ")
