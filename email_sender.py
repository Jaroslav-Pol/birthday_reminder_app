import smtplib
import ssl
from email.message import EmailMessage
from email_settings import sender_email, sender_password, sender_host
from string import Template
from datetime import datetime, timedelta
import time

"""
Please create email_settings.py with your sender email, password and host
"""


def send_emails(data, birthday_list):
    """Sending emails to every person except celebrant.
    to send emails - uncomment 'server.send_message(email)'
    to debug email sending set 'set_debuglevel' to 1, or leave 0
    """
    retry = 0
    context = ssl.create_default_context()  # Creating a secure SSL context

    while retry < 3:
        # If exception raises it will wait 10sec and try again, 3 times max
        try:
            with smtplib.SMTP(host=sender_host, port=587) as server:
                server.ehlo()  # Hi server!
                server.set_debuglevel(0)  # If set to 1 it will display all messages and errors
                server.starttls(context=context)  # Creating secure channel
                server.login(sender_email, sender_password)

                with open('email_message.html', 'r') as email_message:
                    html_message = email_message.read()
                html_template = Template(
                    html_message)  # Creating Template object, which allows us to substitute arguments
                for celebrant in birthday_list:
                    birthdate_formatted = datetime.strftime(datetime.now() + timedelta(days=7), '%A %B %d')
                    #  Formats birthdate to represent weekday, full month name, day e.g.: Sunday March 23
                    for person in data:
                        if person is not celebrant:
                            email = EmailMessage()
                            email['from'] = sender_email
                            email['to'] = person['email']
                            email['subject'] = 'Birthday reminder'
                            data_for_substitution = {'name': person['name'],
                                                     'celebrant_name': celebrant['name'],
                                                     'birthdate': birthdate_formatted,
                                                     'days_left': '7'}
                            email.set_content(html_template.substitute(data_for_substitution), 'html')
                            # server.send_message(email)  # Uncomment to send real emails
                            print(email)
                            time.sleep(3)

        except:  # Need to use it with exact Exceptions, but not sure which can raise
            retry += 1
            time.sleep(10)
            continue

        else:
            break
