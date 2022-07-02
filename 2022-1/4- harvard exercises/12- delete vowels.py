
vowels_list = 'aeiou'

user_input = input('Input: ') #salam chetori?

output = ''

for delete_vowels in user_input:             # sInA
    if delete_vowels.lower() in vowels_list: # i
        pass
    else:
        output += delete_vowels

print(f'Output: {output}')

