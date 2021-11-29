# Read .csv for contacts
# Iterate through contacts
# Check if status is unsent
# Send email
# If email sent, wait 30 sec before sending another
# Check if status is sent
# If sent, see when it was sent
# If 2 months have passed, send an email again
# If 500 emails have been sent, stop sending
import csv
from os.path import exists as exists

contacts_path = 'data/contacts.csv'

with open(contacts_path, 'r') as f:
    