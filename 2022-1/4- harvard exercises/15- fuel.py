
while True:
    try:
        user_input = input('Enter: ').split('/') 
        x = int(user_input[0])
        y = int(user_input[1])
        if (x == 0) or (x == 1 and y == 100):
            print("E")
            break
        if (x == y) or (x == 99 and y == 100):
            print("F")
            break
        if x / y and x < y :
            z = round((x / y) * 100)
            print(f'{z}%')
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except IndexError:
        pass
