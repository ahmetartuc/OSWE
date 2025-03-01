# Get user login information

def user_login():
    print("User Login System")
    print("1. Login")
    print("2. Register")
    
    choice = input("Select an option 1 or 2): ")

    if choice == "1":
        log_in()
    elif choice == "2":
        register()
    else:
        print("Invalid selection! Please enter 1 or 2.")
        user_login()  # Ask again

# If the user registers, write to file

def register():
    username = input("New username: ")
    password = input("Password: ")

    with open("users.txt", "a") as file:
        file.write(username + " " + password + "\n")

    print("Registration successful! You can now log in.")
    user_login()

# If the user logs in, check from file

def log_in():
    username = input("Username: ")
    password = input("Password: ")

    with open("users.txt", "r") as file:
        users = file.readlines()  # Reads all lines

    for user in users:
        saved_username, saved_password = user.strip().split(" ")
        if username == saved_username and password == saved_password:
            print("Successfully logged in!")
            return

    print("Incorrect username or password!")
    log_in()  # Ask again

# Start the main program

user_login()
