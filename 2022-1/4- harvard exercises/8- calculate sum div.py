user_input = input('> ')
user_input = user_input.split(' ')


if user_input[1] == '+':
    result = float(user_input[0]) + float(user_input[2])
    print(result)
elif user_input[1] == '-':
    result = float(user_input[0]) - float(user_input[2])
    print(result)
elif user_input[1] == '*':
    result = float(user_input[0]) * float(user_input[2])
    print(result)
else: # user_input[1] == '/':
    result = float(user_input[0]) / float(user_input[2])
    print(result)
