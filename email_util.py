from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logger import update_log
from time import sleep
from os import environ
import smtplib

def send_email(message):
    server_host = 'smtpout.secureserver.net'
    server_port = 587

    with smtplib.SMTP(server_host, server_port) as server:
        server.starttls()
        server.login(message['From'], environ.get('EMAIL_PASS'))
        server.sendmail(message['From'], message['To'], message.as_string())
        server.quit()

def prepare_message(sender, receiver, subject):
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver

    try:
        plain_text = open('data/email_templates/email_template.txt', encoding='utf-8-sig').read()
        message.attach(MIMEText(plain_text, 'plain'))
        html_text = open('data/email_templates/email_template.html', encoding='utf-8-sig').read()
        message.attach(MIMEText(html_text, 'html'))
    except FileNotFoundError:
        update_log('log.txt', 'Template file(s) does not exist')
    return message

def prepare_and_send(sender, receiver, subject):
    message = prepare_message(sender, receiver, subject)
    send_email(message)
    print('email sent')
    sleep(20)