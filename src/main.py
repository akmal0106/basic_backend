from functions import five_completes_transaction, format_date, split_text, mask_card, mask_account

for i in five_completes_transaction():
    date = format_date(i['date'])
    description = i['description']
    split_to = split_text(i['to'])
    send_to = split_to[0]
    account_to = mask_account(split_to[1])
    amount = i['operationAmount']['amount']
    currency = i['operationAmount'] ['currency'] ['name']
    if description == 'Открытие вклада':
        print(
            f"{date} {description}\n"
            f"{description} -> {send_to} {account_to}\n"
            f"{amount} {currency}\n"
        )
    else:
        split_card = split_text(i['from'])
        if len(split_card) == 2:
            card_name = split_card[0]
            mask = mask_card(split_card[1])
            print(
                f"{date} {description}\n"
                f"{card_name} {mask} -> {send_to} {account_to}\n"
                f"{amount} {currency}\n"
            )
        else:
            card_name = " ".join(split_card[:-1])
            mask = mask_card(split_card[-1])
            print(
                f"{date} {description}\n"
                f"{card_name} {mask} -> {send_to} {account_to}\n"
                f"{amount} {currency}\n"
            )