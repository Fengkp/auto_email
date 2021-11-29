from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logger import update_log
import smtplib

def send_email(message):
    server_host = 'smtpout.secureserver.net'
    server_port = 587

    with smtplib.SMTP(server_host, server_port) as server:
        server.starttls()
        #server.login(message['From'], os.environ.get('EMAIL_PASS'))
        server.sendmail(message['From'], message['To'], message)
        server.quit()

def prepare_message(sender, receiver, subject):
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver

    try:
        plain_text = open('templates/email_template.txt', encoding='utf-8-sig').read()
        message.attach(MIMEText(plain_text, 'plain'))
        html_text = open('templates/email_template.html', encoding='utf-8-sig').read()
        message.attach(MIMEText(html_text, 'html'))
    except FileNotFoundError:
        update_log('log.txt', 'File does not exist')

    return message.as_string()