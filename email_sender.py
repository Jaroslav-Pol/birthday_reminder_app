import smtplib #biblioteka susikalbeti su pasto serveriu
import ssl
from email.message import EmailMessage
from email_settings import sender_email, sender_password, sender_host
from string import Template


# reikia pasiimti reikiamus duomenys is kito failo

with open('email_message.html', 'r') as email_message:
    html_message = email_message.read()

html_template = Template(html_message)

email = EmailMessage()
email['from'] = sender_email
email['to'] = 'polujarek@gmail.com' # pakeisti i receiveremail
email['subject'] = 'Paskutinis testas16,41' # Pakeisti i subject
email.set_content(html_template.substitute({'name': 'Jaroslav'}), 'html') #  Pakeicia reiksmes . Galima arba zodyna, arba per lygu

context = ssl.create_default_context()  # Create a secure SSL context

with smtplib.SMTP(host=sender_host, port=587) as server:
    server.ehlo()# žiūrėkite, kaip į pasisveikinimą su serveriu
    server.set_debuglevel(1) #  If st to 1 it will display all messages and errors
    server.starttls(context=context)# Creating secure chanel
    server.login(sender_email, sender_password)

    server.send_message(email)