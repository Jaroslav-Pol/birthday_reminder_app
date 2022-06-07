"""
Cron (run automatically every day)
Send emails to everyone except person who celebrates one week before birthday
1. Validate persons birthday data file, handle errors
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

import time
from data_validator import parse_data
from birthdays_checker import check_for_birthday
from email_sender import send_emails


def start_app():
    print("Hello!\nIt's birthday reminder app \nPlease choose what you want to do: ")
    time.sleep(1)
    while True:
        print('----------')
        command = input('1. Validate persons data file.\n'
                        '2. Check birthdays, send reminder emails.\n'
                        '9. Exit\n')
        time.sleep(1)
        match command:
            case '1':  # Validate persons data file, returns data if it's valid
                print(
                    'Program will validate persons data file. File should be in JSON format.')
                path_to_file = input('Please enter path and file name: \n')
                data = parse_data(path_to_file)  # Returns data if it's valid, or None
                continue

            case '2':  # Checks for birthdays, send emails
                if 'data' in locals() and data is not None:
                    #  Checks if case 1 was executed before, and or data were valid
                    birthday_list = check_for_birthday(data)
                else:
                    print('Data is not verified, we strongly recommend validate data first')
                    path_to_file = input('Please enter path and file name, or enter 9 to return\n')
                    if path_to_file == '9':
                        continue
                    else:
                        data = parse_data(path_to_file, birthday_check=True)
                        # If birthday_check, then data would be only parsed, not validated

                    if data is not None:
                        birthday_list = check_for_birthday(data)
                    else:
                        continue

                if birthday_list:  # If list is not empty
                    print(f'There are {len(birthday_list)} birthdays after 7 days.')
                    print('Sending emails')
                    time.sleep(2)
                    # input('Send reminder emails y/n?')  # ar nereikia klausti???????????????????
                    send_emails(data, birthday_list)
                    print('Emails successfully sent, program will close in 5 sec')  # Really successfully???????????//
                    time.sleep(5)
                    break
                else:
                    print('Program will close in 5 sec.')
                    time.sleep(5)
                    break
            case '9':  # Exit
                print('Program will close in 5 seconds.')
                time.sleep(5)
                break

            case _:  # Incorrect input
                print('Incorrect input, please try again!')
                continue


if __name__ == '__main__':
    start_app()
