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


import time
from data_validator import parse_data

"""
Reikes gal prideti count errors in data
Reikia padaryti apsauga nuo durniaus, kad negalima butu issiusti emailu, jeigu count_errors nelygus 0
reikia kad atspausdintu kad viskas yra gerai, jeigu viskas yra gerai, galima ji prideti i finaly 
"""





def start_app():
    print('Hello! \nPlease choose what you want to do: ')
    time.sleep(1)  # For testing, maybe need to leave it?
    while True:
        print('----------')
        command = input('1. Validate persons data file.\n'
                        '2. Check for birthdays and send reminder emails.\n'
                        '9. Exit\n')
        time.sleep(1)
        # gal cia reikia kintamuju prideti
        if command == '1':
            print('Program will validate persons data file. File should be in JSON format.')

            #reikia gal cia funkcija padaryti?
            path_to_file = input('Please enter path and file name: \n')
            #  Reikia gal prideti gale .json???
            data = parse_data(path_to_file)
            continue

        elif command == '2':
            if 'data' in locals() and data is not None: #  or we need to use data? patikriname ar data jau yra kaip kintamasis ir jeigu yra, ar nera tuscias
                #  reikia gal dar patikrinti ar buvo errorai, jeigu taip, reikia is pradziu aptikrinti?

                print(data)
                print('labas vakaras')

            else:
                print(data)
                print('Duomenys nepatikrinti, rekomenduojame is pradziu patikrinti duomenys')
                path_to_file = input('Please enter path and file name: \n')
                data = parse_data(path_to_file, birthday_check=True)
                print(data)
            print('')  # Send emails
            time.sleep(3)
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
