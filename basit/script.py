
import re

# Username Validation
def check_username(username):
    pattern = r"^[a-zA-Z0-9_]{4,16}$"

    if re.match(pattern, username):
        return True
    else:
        return False


# Email Validation
def check_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(pattern, email):
        return True
    else:
        return False


# Password Validation
def check_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    if re.match(pattern, password):
        return True
    else:
        return False


# Main Authentication System
print("===== USER AUTHENTICATION SYSTEM =====")

username = input("Enter Username: ")
email = input("Enter Email: ")
password = input("Enter Password: ")

if check_username(username) and check_email(email) and check_password(password):
    print("\nRegistration Successful!")
    print("All validation checks passed.")
else:
    print("\nRegistration Failed!")

    if not check_username(username):
        print("Invalid Username!")

    if not check_email(email):
        print("Invalid Email!")

    if not check_password(password):
        print("Invalid Password!")
