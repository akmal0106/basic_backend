import json
from datetime import datetime
import os

json_file = [file for file in os.listdir() if os.path.splitext(file)[1] == '.json']
file_name = ''.join(json_file)

def load_transactions(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = json.load(f)
        return text

def completed_transactions():
    text = load_transactions(file_name)
    new_line = []
    for operation in text:
        state_info = operation.get('state')
        if state_info == 'EXECUTED':
            new_line.append(operation)
    return new_line

def five_completes_transaction():
    sorted_operations = sorted(completed_transactions(), key=lambda x: x['date'], reverse=True)
    five_operations = []
    for x in range(len(sorted_operations)):
        if len(five_operations) == 5:
            break
        else:
            five_operations.append(sorted_operations[x])
    return five_operations

def format_date(f):
    original_date = datetime.strptime(f, '%Y-%m-%dT%H:%M:%S.%f')
    return original_date.strftime('%d.%m.%Y')

def split_text(text):
    return text.split(' ')

def mask_card(card):
    private_number = card[:6] + (len(card[6:-4]) * '*') + card[-4:]
    divide_number = [private_number[i:i+4] for i in range(0, len(private_number),4)]
    return " ".join(divide_number)

def mask_account(account):
    private_account = (len(account[-6:-4]) * '*') + account[-4:]
    return private_account

