# 1
# Saving progress.
# Make a function that takes personal information as arguments, e.g., name,
# last name, phone number, address, etc. Then make another function that saves
# the data onto a file. Make sure that it works by checking that the file was
# created and that it contains the right data.

import json


def get_personal_information():
    user_info = {}

    user_info['name'] = input('What is your name? ')
    user_info['last_name'] = input('What is your last name? ')
    user_info['phone'] = input('What is your phone number? ')
    user_info['address'] = input('What is your address? ')

    return user_info


def write_information(user_info):
    with open('user_info.txt', 'w') as file_objec:
        user_info_json = json.dumps(user_info)
        file_objec.write(user_info_json)


info = get_personal_information()

write_information(info)

# 2
# Add to the previous program a function for opening up the same file which
# the data was saved on. Make sure that it works by making the function print
# out the data.


def show_file():
    with open('user_info.txt') as user_file:
        user_info = user_file.read()
        print(user_info)


show_file()
