from datetime import datetime, timedelta
import calendar

birthday_list = []


def check_for_birthday(data):
    """Checking for upcoming birthdays, if there are - returns birthday_list"""
    for person in data:
        birthdate = person['birthdate']
        date_after_week = (datetime.today() + timedelta(days=7)).strftime('%m-%d')
        # Formatting date after 7 days to MM-DD and makes str from it

        if date_after_week == birthdate[-5:]:  # Checks last 5 elements in date, which are MM-DD
            print(f"Person {person['name']} birthday after 7 days!")
            birthday_list.append(person)

        elif birthdate == '02-29' and date_after_week == '03-01' and not calendar.isleap(datetime.today().year):
            # If birthday is on 02-29 and this is not leap year
            print(f"Person {person['name']} birthday after 7 days!")
            print(f"{person['name']} was born on 02-29, don't let him/her cry! Let's celebrate anyway!")
            birthday_list.append(person)

    if birthday_list:  # If list is not empty
        return birthday_list
    else:
        print('There is no upcoming birthdays after 7 days')
