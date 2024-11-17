__author__      = "Karim BAJEDDI"
__copyright__   = "NC"

from flask import Flask, send_file, request
import datetime
import subprocess, json
from sender import send_notif

f = open('mail.json')
mail = json.load(f)

app = Flask(__name__)

@app.route('/p0.png')
def send_image():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip_address = request.remote_addr
    user_agent = request.user_agent
    headers = request.headers
    info = f'p0 {timestamp} - IP: {ip_address}, User-Agent: {user_agent}, Headers: {headers}\n'
    subprocess.run(f"echo '{info}' >> /home/saru/logs/log.txt", shell=True)

    response = send_file('p.png', mimetype='image/png')
    response.headers.add('Access-Control-Allow-Origin', '*')
    open('recieve_log.txt').write(f'\n[✓] email {mail["emails"][0]} was opened by the reciever.')
    send_notif(mail['emails'][0])

    return response

@app.route('/p1.png')
def send_image():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip_address = request.remote_addr
    user_agent = request.user_agent
    headers = request.headers
    info = f'p1 {timestamp} - IP: {ip_address}, User-Agent: {user_agent}, Headers: {headers}\n'
    subprocess.run(f"echo '{info}' >> /home/saru/logs/log.txt", shell=True)

    response = send_file('p.png', mimetype='image/png')
    response.headers.add('Access-Control-Allow-Origin', '*')
    open('recieve_log.txt').write(f'\n[✓] email {mail["emails"][1]} was opened by the reciever.')
    send_notif(mail['emails'][1])

    return response

@app.route('/p2.png')
def send_image():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip_address = request.remote_addr
    user_agent = request.user_agent
    headers = request.headers
    info = f'p2 {timestamp} - IP: {ip_address}, User-Agent: {user_agent}, Headers: {headers}\n'
    subprocess.run(f"echo '{info}' >> /home/saru/logs/log.txt", shell=True)

    response = send_file('p.png', mimetype='image/png')
    response.headers.add('Access-Control-Allow-Origin', '*')
    open('recieve_log.txt').write(f'\n[✓] email {mail["emails"][2]} was opened by the reciever.')
    send_notif(mail['emails'][2])

    return response

@app.route('/p3.png')
def send_image():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip_address = request.remote_addr
    user_agent = request.user_agent
    headers = request.headers
    info = f'p3 {timestamp} - IP: {ip_address}, User-Agent: {user_agent}, Headers: {headers}\n'
    subprocess.run(f"echo '{info}' >> /home/saru/logs/log.txt", shell=True)

    response = send_file('p.png', mimetype='image/png')
    response.headers.add('Access-Control-Allow-Origin', '*')
    open('recieve_log.txt').write(f'\n[✓] email {mail["emails"][3]} was opened by the reciever.')
    send_notif(mail['emails'][3])

    return response

@app.route('/p4.png')
def send_image():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip_address = request.remote_addr
    user_agent = request.user_agent
    headers = request.headers
    info = f'p4 {timestamp} - IP: {ip_address}, User-Agent: {user_agent}, Headers: {headers}\n'
    subprocess.run(f"echo '{info}' >> /home/saru/logs/log.txt", shell=True)

    response = send_file('p.png', mimetype='image/png')
    response.headers.add('Access-Control-Allow-Origin', '*')
    open('recieve_log.txt').write(f'\n[✓] email {mail["emails"][4]} was opened by the reciever.')
    send_notif(mail['emails'][4])

    return response

@app.route('/p5.png')
def send_image():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip_address = request.remote_addr
    user_agent = request.user_agent
    headers = request.headers
    info = f'p5 {timestamp} - IP: {ip_address}, User-Agent: {user_agent}, Headers: {headers}\n'
    subprocess.run(f"echo '{info}' >> /home/saru/logs/log.txt", shell=True)

    response = send_file('p.png', mimetype='image/png')
    response.headers.add('Access-Control-Allow-Origin', '*')
    open('recieve_log.txt').write(f'\n[✓] email {mail["emails"][5]} was opened by the reciever.')
    send_notif(mail['emails'][5])

    return response


"""
add as much as you want from this block of code to increase the emails that you can track (you can track an infinit on emails),
keep in mind that you need to change the route for e.g /p5.png -> /p6.png -> /p7.png ....

@app.route('/p5.png')
def send_image():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip_address = request.remote_addr
    user_agent = request.user_agent
    headers = request.headers
    info = f'p5 {timestamp} - IP: {ip_address}, User-Agent: {user_agent}, Headers: {headers}\n'
    subprocess.run(f"echo '{info}' >> /home/saru/logs/log.txt", shell=True)

    response = send_file('p.png', mimetype='image/png')
    response.headers.add('Access-Control-Allow-Origin', '*')
    open('recieve_log.txt').write(f'\n[✓] email {mail["emails"][5]} was opened by the reciever.')
    send_notif(mail['emails'][5])

    return response
    
    
"""


if __name__ == '__main__':
    app.run()
