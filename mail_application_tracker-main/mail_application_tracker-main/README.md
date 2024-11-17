# Email Tracking and Notification System
Made by Youssef EL MANSOURI

![Logo](https://elmansouri-port.github.io/assets/project-2.jpeg)
## Overview

This project consists of two Python scripts: `sender.py` and `server_track.py`. The `sender.py` script sends emails to a list of recipients and logs the status of each email sent. The `server_track.py` script is a Flask web server that serves image files and tracks when recipients open the emails, sending a notification when an email is opened.

## Installation

### Dependencies

- [Python 3](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [mailer](https://pypi.org/project/mailer/)


Copy code
python sender.py
server_track.py
Update the mail.json file with the same list of email addresses.

Run the server script:

Copy code
python server_track.py
use www.pythonanywhere.com to host your server to be online and use it over the internet.
Access the tracked images using URLs like http://localhost:5000/p0.png, http://localhost:5000/p1.png, etc. or [http://www.myaccount_name.pythonanywhere.com/p1.png]

Contributing
Feel free to contribute to this project by forking and submitting a pull request. Follow the guidelines in CONTRIBUTING.md.

License
This project is open for anny one to use it.

csharp
Copy code


```bash
pip install Flask
pip install mailer
Usage
sender.py
Create a mail.json file with a list of email addresses under the key 'emails'.

json
Copy code
{
  "emails": ["recipient1@example.com", "recipient2@example.com", "recipient3@example.com"]
}
Update the email sender details and customize the email content in sender.py.

Run the sender script
