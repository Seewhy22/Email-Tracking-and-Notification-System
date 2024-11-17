__author__      = "Youssef EL MANSOURI"
__copyright__   = "NC"

import json
from mailer import Mailer
from time import sleep
from random import randint

f = open('mail.json')
Mail = json.load(f)

mail = Mailer(email='youssefx8383@gmail.com',
              password='application pass')

def send_aplication():

  start = 0

  for mail in Mail['emails']:
    m = Mail['emails'][start]
    mail.send(receiver=f'{m}',  
              no_reply='noreplay@example.com',
              subject='APLICATION FOR AN INTERNSHIP ON MARKETING DATA MANIPULATION AND FINANCE.(YOUSSEF EL MANSOURI)',
              message=f"""<span> your html here <strong> Youssef EL MANSOURI </strong></span>""")

    status = mail.status
    log = open('send_log.txt')
    if status == True:
      log.write(f'\n[✓]{mail.status}')
    else:
      log.write(f'\n[!!!]{mail.status}[!!!]')
    log.close()

    start += 1

    sleep(randint(60,1000))


def send_notif(mail):

  mail.send(receiver='receiver@mail.com',
            no_reply='noreplay@example.com',
            subject='{mail} opened the sent email',
            message='')
  
