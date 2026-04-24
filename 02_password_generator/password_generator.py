"""
Mini-project #4: Password Generator
"""

import string, random

# setup
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
all_characters = lowercase_letters + uppercase_letters + digits + symbols

def generate_password():
    password = ""
    while True:
        try: # take length
            password_length = int(input("Enter password length: "))
            if password_length < 4 or password_length > 128:
                print("Password length must be between 4 and 128")
                continue
        except ValueError: # verify it
            print("Password length must be between 4 and 128")
            continue

        # make sure the password contains at least 1 of each data type
        password += random.choice(lowercase_letters)
        password += random.choice(uppercase_letters)
        password += random.choice(digits)
        password += random.choice(symbols)

        # creating the password
        while len(password) < password_length:
            password += random.choice(all_characters)

        # shuffle for more security
        password_list = list(password)
        random.shuffle(password_list)
        password = "".join(password_list)

        print(f"Generated password is: {password}")
        break

if __name__ == "__main__":
    while True:
        generate_password()  # run program

        # ask user if they want to repeat
        repeat = input("\nGenerate another password? (y/n): ").strip().lower()
        if repeat != 'y':
            print("Exiting... Stay secure! 🔐")
            break