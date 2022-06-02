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
# df  = pd.read_json('employees.json')
# #
# # print(df)
# print(df.eq('').values.any()) #Suranda ar trukta kurios nors eilutes, arba null reikai patikrinti
import json

def validate_birthdate(birthdate):
    pass

def validate_email(email):
    pass

def validate_person_data(data):
    for person in data:
        # print(person)
        if bool(person['name'].strip()) and bool(person['email'].strip() and bool(person['birthdate'].strip())):
            #  Checks if there is no empty items
            validate_birthdate(person['birthdate'])
            validate_email(person['email'])
            print('all ok')
        else:
            print(f'bad news, there is a person with empty : {person}')




def parse_data(json_file_name):# check if parsing data is ok, add some logic, more exceptions
    try:
        with open(json_file_name) as json_file:
            data = json.load(json_file)
            print(data)
    except ValueError:
        print('Data file should be in JSON format!!!')
    else:
        validate_person_data(data)
    finally:
        pass




if __name__ == '__main__':
    parse_data('employees.json')

