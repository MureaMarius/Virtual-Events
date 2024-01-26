import random


def password_validation(my_pass: str):
    number_of_lowercase = 0
    number_of_uppercase = 0
    number_of_digits = 0
    number_of_special_chars = 0

    for x in my_pass:
        if x.isalpha() and x.isupper():
            number_of_uppercase += 1
        elif x.isalpha() and x.islower():
            number_of_lowercase += 1
        elif x.isdigit():
            number_of_digits += 1
        elif not x.isalpha():
            number_of_special_chars += 1

    if len(my_pass) < 10 or number_of_special_chars < 1 or number_of_lowercase < 1 or number_of_uppercase < 1:
        return False

    return True


def create_random_password():
    global selected_string
    resulted_pass = ""
    letters_lower_case = "qwertyuiopasdfghjklzxcvbnm"
    letters_upper_case = letters_lower_case.upper()
    special_chars = "!@#$*"
    digits = "0123456789"

    my_list_of_random_chars = [letters_upper_case, letters_lower_case, special_chars, digits]
    while True:
        selected_string = my_list_of_random_chars[random.randint(0, len(my_list_of_random_chars) - 1)]
        resulted_pass += selected_string[random.randint(0, len(selected_string) - 1)]

        if password_validation(resulted_pass):
            return resulted_pass


def check_users(username: str, email: str, list_of_users: list):
    for user in list_of_users:
        if user[1] == username:
            return "Invalid username -- try another one"
        elif user[3] == email:
            return "Email already used"

    return None
