user_input = input('Enter 42: ')

if user_input.replace(" ", "") == '42':
    print('Yes')
elif user_input.lower().strip() == 'forty two' or user_input.lower().strip() == 'forty-two': # forty two
    print('Yes')
else:
    print('No')
