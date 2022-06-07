import json
from datetime import datetime, timedelta
import time

error_list = []


def parse_data(path_to_file, birthday_check=False):
    """Checking if data parsing is ok, if yes, sending data for validation
    or we need to return it better?
    if birthday_check, we are not checking data, only opening file and send it back"""
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
            data = data['persons']
            # Checking is data from json file is dict with table name, if so, converts it to list only with dict values
        if birthday_check:
            return data
        else:
            validate_person_data(data)
            # if we return bad data? is it ok?
            if not error_list:
                # If there is no errors
                return data  # ??? ar reikia
            else:
                return
                # pass #  ka cia reikia? a1r reikia?


def validate_person_data(data):
    """Validates for empty elements in data, if it's ok, then checking date and email"""
    error_list.clear()
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
    if len(error_list) > 0:
        print(f'Found {len(error_list)} errors with data, please check!')  # Maybe add names from error list?
    else:
        print('Data is OK!')
        #  return ??


def validate_email(person):
    """Simple email validator, check's if @ or . is in string"""
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
                birthday_date = datetime.strptime(person['birthdate'], '%m-%d')  ## gal cia reikia pasalinti kintamaji?
            except ValueError:
                print(error_message)
                error_list.append(person['name'])

    else:
        print(error_message)
        error_list.append('+')
