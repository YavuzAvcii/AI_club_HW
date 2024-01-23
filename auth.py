username = "Yavuz"
password = "asdfgh"
i_username = input("Please enter your username ")
i_password = input("Please enter your password ")


def auth(i_username, i_password):
    if (i_username == username and i_password == password):
        print("Logged in!")
    else:
        print("username or password is incorrect")



auth(i_username, i_password);