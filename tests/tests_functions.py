import pytest
import json
from src.functions import load_transactions, completed_transactions, five_completes_transaction, format_date, split_text, mask_card, mask_account
import os

json_file = [file for file in os.listdir() if os.path.splitext(file)[1] == '.json']
file_name = ''.join(json_file)

def test_load_transactions():
    assert len(load_transactions(file_name)) == 9

def test_completed_transactions():
    assert len(completed_transactions()) == 7

def test_five_completes_transaction():
    assert len(five_completes_transaction()) == 5

def test_format_date():
    assert format_date('2018-12-20T16:43:26.929246') == '20.12.2018'

def test_split_text():
    assert split_text('Visa Gold 3589276410671603') == ['Visa', 'Gold', '3589276410671603']

def test_mask_card():
    assert mask_card('1596837868705199') == '1596 83** **** 5199'

def test_mask_account():
    assert mask_account('1596837868705199') == '**5199'