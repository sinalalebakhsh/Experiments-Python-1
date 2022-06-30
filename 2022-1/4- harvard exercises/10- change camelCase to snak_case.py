user_input = input('camelCase: ')

finall_input = ''

first_char = user_input[0]

if first_char.isupper():
    first_char = first_char.lower()
    user_input =  user_input[1:]
    user_input = first_char + user_input


for s in user_input:
    if s.isupper():
        finall_input += '_' + s.lower()
    else:
        finall_input += s

print(finall_input)
