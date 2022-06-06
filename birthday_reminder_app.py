"""
Cron (run automaticaly every day)
Send emails to everyone except person who celebrates
One week before birthday
1. Valdate persons birthday data file, handle errors
     A person's entry in the file will contain:
        1.the person's name,
        2.email,
        3.birthdate (in YYYY-MM-DD or MM-DD format).
    The data file is considered valid if:
    •it can be successfully parsed,
    •all people have a name set,
    •all people have an email set (however, you don't need to check if the email addresses are  valid or not),
    •each person's birthdate is a valid date (eg. no 02-30 or 01-32) in the PAST.

2. Check for upcoming birthdays and send emails if there are any.
    1.the emails can always be sent successfully in 3 retries,
    2.emails are sent instantly (there is no need to send the emails asynchronously),
    3.the email template is hardcoded.

Exit once emails are sent.
Interface CLI
"""

import json
from datetime import datetime, timedelta
import time

error_list = []

"""
Reikes gal prideti count errors in data
Reikia padaryti apsauga nuo durniaus, kad negalima butu issiusti emailu, jeigu count_errors nelygus 0
reikia kad atspausdintu kad viskas yra gerai, jeigu viskas yra gerai, galima ji prideti i finaly 
"""


def parse_data(json_file_name):
    """Checking if data parsing is ok, if yes, sending data for validation
    or we need to return it better?"""
    try:
        with open(json_file_name) as json_file:
            data = json.load(json_file)
    except ValueError:
        print('Data file should be in JSON format!!!\n----------')
    except FileNotFoundError and OSError:
        print('File not found! Please enter correct path and filename.\n-----------')
    else:
        # Sending parsed data for validation
        print('Data parsing is ok.\n----------')
        time.sleep(2)
        if type(data) == list:
            # Checking is data from json file with table name or without
            validate_person_data(data)
        elif type(data) == dict:
            validate_person_data(data['persons'])

    finally:
        pass


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


def start_app():
    print('Hello! \nPlease choose what you want to do: ')
    time.sleep(1)  # For testing, maybe need to leave it?
    while True:
        print('----------')
        command = input('1. Validate persons data file.\n'
                        '2. Check for birthdays and send reminder emails.\n'
                        '9. Exit\n')
        time.sleep(1)
        if command == '1':
            print('Program will validate persons data file. File should be in JSON format.')
            path_to_file = input('Please enter path to the file: \n')
            file_name = input('Please enter file name: \n')
            # time.sleep(1)
            if not path_to_file:
                #  If path is a program folder
                parse_data(file_name)
            else:
                parse_data(path_to_file + '\\' + file_name)
            continue

        elif command == '2':
            print('')  # Send emails
            time.sleep(5)
            print('emails successfully sent')
            break

        elif command == '9':
            print('Program successfully closed!')
            time.sleep(2)
            break

        else:
            print('Incorrect input, please try again!')
            continue


if __name__ == '__main__':
    start_app()
