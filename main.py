
# Check if status is sent
# If sent, see when it was sent
# If 2 months have passed, send an email again
# If 500 emails have been sent, stop sending

import pandas as pd
from csv import reader as reader
from os.path import exists as exists
from os import environ
from email_util import prepare_and_send
from datetime import datetime

def send_unsent(path, sender, subject):      
    data = pd.read_csv(path)
    for index, row in data.iterrows():
        if 'Unsent' in row['Status']:
            receiver = data.loc[index, 'Email']
            prepare_and_send(sender, receiver, subject)
            data.loc[index, 'Status'] = 'Sent'
            data.loc[index, 'Send Date'] = datetime.now()
    data.to_csv(path, index=False)

def set_unsent(path):
    data = pd.read_csv(path)
    for index, row in data.iterrows():
        if pd.isnull(row['Status']):
            data.loc[index, 'Status'] = 'Unsent'
    data.to_csv(path, index=False)

contacts_path = 'data/contacts.csv'
subject = 'Pipe Supply for Projects'
username = environ.get('MY_EMAIL')
set_unsent(contacts_path)
send_unsent(contacts_path, username, subject)