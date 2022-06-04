import smtplib  # biblioteka susikalbeti su pasto serveriu
import ssl
from email.message import EmailMessage
from email_settings import sender_email, sender_password, sender_host
from string import Template
import time


# def send_emails(data, birthday_list):
#     print(data)
#     print(birthday_list)
#     for celebrant in birthday_list:
#
#         print(f'I am celebrant {celebrant}')
#         for person in data:
#             if person is not celebrant:
#                 print(f'I am person {person}')
#             # send email (person, birthday lisit)


"""
Dabara reikies prideti kintamuosius ir sudeti viska i funkcija

"""


# reikia pasiimti reikiamus duomenys is kito failo
def send_emails(data, birthday_list):
    context = ssl.create_default_context()  # Create a secure SSL context

    with smtplib.SMTP(host=sender_host, port=587) as server:
        server.ehlo()  # žiūrėkite, kaip į pasisveikinimą su serveriu
        server.set_debuglevel(1)  # If st to 1 it will display all messages and errors
        server.starttls(context=context)  # Creating secure chanel
        server.login(sender_email, sender_password)

        with open('email_message.html', 'r') as email_message:
            html_message = email_message.read()
        html_template = Template(html_message)
        for celebrant in birthday_list:
            for person in data:
                if person is not celebrant:
                    email = EmailMessage()
                    email['from'] = sender_email
                    email['to'] = person['email']  # pakeisti i receiveremail
                    email['subject'] = f'Birthday reminder'
                    # Pakeisti i subject, reikia kad prisidetu vardas dar celebratora
                    data_for_substitution = {'name': person['name'],
                                             'celebrant_name': celebrant['name'],
                                             'birthdate': person['birthdate'][-5:],
                                             'days_left': '7'} # reikia gal days_left padaryti kintamaji

                    email.set_content(html_template.substitute(data_for_substitution), 'html')
                    server.send_message(email)
                    print(email)
                    # cia gal reikia prideti laukima?
                    time.sleep(5)




""" reikia pratestuoti ar veikia tokia sistema su savo emailais
 padaryti emailo templata
 padaryti subject
 padaryti emaile kad rodytu normalia data vietoje skaiciu pvz march 30(bet jei bus laiko) nebutimnai
 """

# with open('email_message.html', 'r') as email_message:
#     html_message = email_message.read()
# html_template = Template(html_message)
#
# email = EmailMessage()
# email['from'] = sender_email
# email['to'] = 'polujarek@gmail.com'  # pakeisti i receiveremail
# email['subject'] = 'Paskutinis testas16,41'  # Pakeisti i subject
# email.set_content(html_template.substitute({'name': 'Jaroslav'}),
#                   'html')  # Pakeicia reiksmes . Galima arba zodyna, arba per lygu
#
# context = ssl.create_default_context()  # Create a secure SSL context
#
# with smtplib.SMTP(host=sender_host, port=587) as server:
#     server.ehlo()  # žiūrėkite, kaip į pasisveikinimą su serveriu
#     server.set_debuglevel(1)  # If st to 1 it will display all messages and errors
#     server.starttls(context=context)  # Creating secure chanel
#     server.login(sender_email, sender_password)
#
#     server.send_message(email)
