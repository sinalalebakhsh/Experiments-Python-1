import re

def main():
    user_input = input("user_input: ")  #si11
    if is_valid(user_input):
        print("Valid")
    else:
        print("Invalid")

def is_valid(user_input):
    if user_input[:2].isalpha():
        if len(user_input) >= 2 and len(user_input) <= 6:
            if ' ' in user_input:
                return False
            if '.' in user_input:
                return False
            number_in_user_input = re.findall(r'\d+', user_input) # ['11']
            if number_in_user_input == []:
                return True
            elif number_in_user_input[0][0] != '0': #['11'] '11' '1'
                if len(number_in_user_input) == 1 and user_input[-1].isdigit() :
                    return True
    else:
        return False


main()
