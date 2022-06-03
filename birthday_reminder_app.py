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
from datetime import datetime

def validate_birthdate(birthdate):
    # reikia dar patikrinti jeigu gimtadienis 02.29 kad pranestu 02.28
    # reikia kad data butu praeityje

    if len(birthdate) == 10:
        try:
            birthday_date = datetime.strptime(birthdate, '%Y-%m-%d')
            if birthday_date > datetime.now():
                #  patikrina ar gimtadienis yra praeityje
                print('Person is not born yet')
                raise ValueError

        except ValueError:
            print('Incorrect date format or date is out of range, it should be YYYY-MM-DD or MM-DD')
            print(birthdate)
        else:
            print('viskas ok')
    elif len(birthdate) == 5:
        if birthdate.endswith('02-29'):
            # If birthday is 02-29 it will act like birthday is on 02-28
            print('abrakadabra')
            birthdate = '02-28' # kad ansciau pranestu
        try:
            birthday_date = datetime.strptime(birthdate, '%m-%d')
        except ValueError:
            print('Incorrect date format or date is out of range, it should be YYYY-MM-DD or MM-DD')
        else:
            print('cia irgi ok')

    else:
        print('Incorrect date format or date is out of range, it should be YYYY-MM-DD or MM-DD')


def validate_email(email):
    if '@' not in email or '.' not in email:
        print('email is not correct')


def validate_person_data(data):
    for person in data:
        # print(person)
        if bool(person['name'].strip()) and bool(person['email'].strip() and bool(person['birthdate'].strip())):
            #  Checks if there is no empty items
            validate_birthdate(person['birthdate'])
            validate_email(person['email'])
            print('----------------')
        else:
            print(f'bad news, there is a person with empty data: {person}')
            print('-----------------')




def parse_data(json_file_name):# check if parsing data is ok, add some logic, more exceptions
    try:
        with open(json_file_name) as json_file:
            data = json.load(json_file)
            print(data)
    except ValueError:
        print('Data file should be in JSON format!!!')
    except FileNotFoundError:
        print('File not found!')
    else:
        validate_person_data(data)
    finally:
        pass




if __name__ == '__main__':
    parse_data('persons.json')

