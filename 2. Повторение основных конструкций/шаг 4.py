def hide_card(card_number):
    clear_number = card_number.replace(' ', '')
    censored_number = '*' * 12 + clear_number[12:]
    return censored_number

card = '905 678123 45612 56'

print(hide_card(card))

