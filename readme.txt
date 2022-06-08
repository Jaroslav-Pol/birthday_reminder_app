- Before running, please create email_settings.py with your sender email, password and host

- json file should be like:
[
  {
    "name": "John Smith",
    "email": "john@smith.com",
    "birthdate": "MM-DD" or "YYYY-MM-DD"
  },
]
or
{
  "persons": [
    {
      "name": "John Smith",
      "email": "john@smith.com",
      "birthdate": "MM-DD" or "YYYY-MM-DD"
    },
  ]
}

- To run script please run birthday_reminder_app.py, use python 3.10

- To send real emails please uncomment 'server.send_message(email) in email_sender.py,
otherwise mails will be only printed in cl

- To see more info about email sending, please 'set_debuglevel' to 1 in email_sender.py

