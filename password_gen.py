import random
import string

def get_password():
    # Initial password generation
    while True:
        user_input = input("Enter a number: ")
        try:
            length = int(user_input)
            password = ""
            characters = (string.ascii_lowercase + string.digits)
            for i in range(length):
                password += random.choice(characters)
            print("Here's your new password:" + " " + password)
            check_password_strength(password)        
            break
        except ValueError:
            print("Im sorry, that is not a valid number. Try again.")


def check_password_strength(password):
    password_length = len(password)
    print ("Your password length is:" + " " + str(password_length))
    has_number = False
    for character in password:
        if character.isdigit():  # isdigit() checks if a character is a number
            has_number = True
            break  # Found one, no need to keep looking

    if has_number:
        print("✓ Contains numbers")
    else:
        print("✗ No numbers found")

    has_letter = False
    for character in password:
        if character.isalpha():
            has_letter = True
            break

    if has_letter:
        print("✓ Contains letters")
    else:
        print("✗ No letters found")
            

get_password()