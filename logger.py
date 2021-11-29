import os
from datetime import datetime

def create_log(path):
    with open(path, 'w') as f:
        f.write(f'{datetime.now()}: log created\n')

def update_log(path, message):
    if not os.path.exists(path):
        create_log(path)
    with open(path, 'a+') as f:
        f.write(f'{datetime.now()}: {message}\n')