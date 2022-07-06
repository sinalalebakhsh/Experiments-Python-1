dict_nurition = {
    'apple' : '130',
    'Avocado' : '50',
    'Sweet Cherries' : '100',
    'banana' : '110',
    'Kiwifruit' : '90',
    'pear' : '100',
}

user_input = input('Item: ')

if user_input in dict_nurition.keys():
    if user_input == 'apple':
        print('Calories: 130')
    elif user_input == 'Avocado':
        print('Calories: 50')
    elif user_input == 'Sweet Cherries':
        print('Calories: 100')
    elif user_input == 'Kiwifruit':
        print('Calories: 90')
    elif user_input == 'pear':
        print('Calories: 100')
    elif user_input == 'banana':
        print('Calories: 110')
