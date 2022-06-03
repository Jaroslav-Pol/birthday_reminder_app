from datetime import datetime, timedelta
import json

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
       check_for_birthday(data)
    finally:
        print(data)


def check_for_birthday(data): # or data? or json?????
    for person in data:
        birthdate = person['birthdate']
        date_after_week = (datetime.today() + timedelta(days=7)).strftime('%m-%d')  # Formated date to str after 7 days
        if len(birthdate) == 10:
            if date_after_week == birthdate[-5:]:
                print(f"Person {person['name']} birthday after 7 days!")
                person['birthday_after_7_days'] = True
            else:
                person['birthday_after_7_days'] = False

        elif len(birthdate) == 5:
            if birthdate.endswith('02-29'):
                # If birthday is 02-29 it will act like birthday is on 02-28
                birthdate = '02-28'  # kad ansciau pranestu,

            if date_after_week == birthdate:
                print(f"Person {person['name']} birthday also after 7 days!")
                person['birthday_after_7_days'] = True
            else:
                person['birthday_after_7_days'] = False

        else:
            print('Something went wrong, please validate persons data first!')


parse_data('persons_validated.json')

