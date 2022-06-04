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

# import pandas as pd
# df  = pd.read_json('persons.json')
# #
# # print(df)
# print(df.eq('').values.any()) #Suranda ar trukta kurios nors eilutes, arba null reikai patikrinti
import json
from datetime import datetime, timedelta


def parse_data(json_file_name):
    """main function"""
    # check if parsing data is ok, add some logic,
    # Checks if we can succesfuly load data from file, if yes, then we send it to validation
    try:
        with open(json_file_name) as json_file:
            data = json.load(json_file)
            print(data)
            print(type(data))
    except ValueError:
        print('Data file should be in JSON format!!!')
    except FileNotFoundError:
        print('File not found!')
    else:
        # sending parsed data for validation
        validate_person_data(data) # if data starts with person(table name) then we need to data['person']
    finally:
        pass


def validate_person_data(data):
    """This f-n validates for empty elements in data"""
    for person in data:
        # print(person)
        if bool(person['name'].strip()) and bool(person['email'].strip() and bool(person['birthdate'].strip())):
            #  Checks if there is no empty items
            # If all rows are not empty, then we send tada to next step. Validate birthdate and validate email
            validate_birthdate(person)
            validate_email(person)
            print('----------------')
        else:
            print(f'bad news, there is a person with empty data: {person}')
            print('-----------------')
    print(data)


def validate_email(person):
    """Simple email validator, check's if @ or . is in string"""
    if '@' not in person['email'] or '.' not in person['email']:
        print(f'Person {person["name"]} email is not correct, please check it!')


def validate_birthdate(person, birthday_check=False):
    # reikia dar patikrinti jeigu gimtadienis 02.29 kad pranestu 02.28
    # reikia kad data butu praeityje

    error_message = f"Person's {person['name']} birthdate {person['birthdate']} format is incorrect " \
                    f"or date is out of range, it should be YYYY-MM-DD or MM-DD"

    if len(person['birthdate']) == 10:
        try:
            birthday_date = datetime.strptime(person['birthdate'], '%Y-%m-%d')
            if birthday_date > datetime.now():
                #  patikrina ar gimtadienis yra praeityje
                print(f'Person {person["name"]} is not born yet')
                raise ValueError #?? do we need this? if not, then it will execut else

        except ValueError:
            print(error_message)
        else:
            print('viskas ok') #  jeigu viskas ok, galime grazinti duomenys
            # person['birthday_date'] = birthday_date
            # print(person)
            # print(type(person['birthday_date']))

    elif len(person['birthdate']) == 5:
        if person['birthdate'].endswith('02-29'):
            # If birthday is 02-29 it will act like birthday is on 02-28, otherwise it throws error
            print('abrakadabra')
            person['birthdate'] = '02-28'  # kad ansciau pranestu
        try:
            birthday_date = datetime.strptime(person['birthdate'], '%m-%d')
        except ValueError:
            print(error_message)
        else:
            print('cia irgi ok')

    else:
        print(error_message)




if __name__ == '__main__':
    parse_data('persons.json')
