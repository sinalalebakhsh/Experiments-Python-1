amount_due = 50

while amount_due != 0:
    print(f'Amount Due: {amount_due}')
    insert_coin = int(input('Insert Coin: '))
    if amount_due >= insert_coin:
        if insert_coin == 25:
            amount_due = amount_due - 25
        elif insert_coin == 10:
            amount_due = amount_due - 10
        elif insert_coin == 5:
            amount_due = amount_due - 5
    elif amount_due < insert_coin and insert_coin == 25 or insert_coin == 5  :
        amount_due -= 5
        print(amount_due)
        break

if amount_due == 0:
    print(f'Change owed: {amount_due}')
