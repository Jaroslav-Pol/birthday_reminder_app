import json
from datetime import datetime, timedelta
import time

error_list = []


def parse_data(path_to_file, birthday_check=False):
    """Parsing data, if ok, sending it for validation. Returns data if it's validated.
    if birthday_check - not validating data, only parsing file and returns it"""
    try:
        with open(path_to_file) as json_file:
            data = json.load(json_file)
    except ValueError:
        print('Data file should be in JSON format!!!\n----------')
    except FileNotFoundError and OSError:
        print('File not found! Please enter correct path and filename.\n-----------')
    else:
        # Sending parsed data for validation, or to birthday check
        print('Data parsing is ok.\n----------')
        time.sleep(2)

        if type(data) == dict:
            # Checking is data from json file is dict with table name, if so, converts it to list with dict values
            data = data['persons']
        if birthday_check:
            # Returning data without checking it
            return data
        else:
            validate_person_data(data)
            #  Sending data for validation
            if not error_list:
                # If there is no errors
                return data


def validate_person_data(data):
    """Validates for empty elements in data, if ok  - checks date and email"""
    error_list.clear()  # If there was previous validations, clears error list
    for person in data:
        if bool(person['name'].strip()) and bool(person['email'].strip() and bool(person['birthdate'].strip())):
            # Checks if there is no empty items
            validate_birthdate(person)
            # Checks birthday date
            validate_email(person)
            # Checks email
        else:
            print(f'There is a person with empty data: {person}\n----------')
            error_list.append(person['name'])

    if error_list:
        # If there are some errors
        print(f'Found {len(error_list)} errors with data, please check!')
    else:
        print('Data is valid!')


def validate_email(person):
    """Simple email validator, checks if '@' or '.' is in string"""
    if '@' not in person['email'] or '.' not in person['email']:
        print(f'Person {person["name"]} email is not correct, please check it!\n----------')
        error_list.append(person['name'])


def validate_birthdate(person):
    """Validates person birthday date"""
    error_message = f"Person's {person['name']} birthdate {person['birthdate']} format is incorrect " \
                    f"or date is out of range, it should be YYYY-MM-DD or MM-DD!\n----------"

    if len(person['birthdate']) == 10:
        # If date format is YYYY-MM-DD
        try:
            birthday_date = datetime.strptime(person['birthdate'], '%Y-%m-%d')
            #  Try to make date object from string, if succeed - date is valid
            if birthday_date > datetime.now():
                #  Checks if date is in past
                print(f'Person {person["name"]} is not born yet!\n----------')
                error_list.append(person['name'])

        except ValueError:
            print(error_message)
            error_list.append(person['name'])

    elif len(person['birthdate']) == 5:
        #  If date format is MM-DD
        if person['birthdate'] == '02-29':
            pass
        else:
            try:
                datetime.strptime(person['birthdate'], '%m-%d')
                #  Try to make date object from string, if succeed - date is valid

            except ValueError:
                print(error_message)
                error_list.append(person['name'])

    else:
        print(error_message)
        error_list.append(person['name'])
