
with open('hash.txt' , 'r') as file:
    line_number = 0
    for i in file.readlines():
        line_number += 1
        if i == 'b4488598eaf2fd27f71f427a169b7684\n':
            print(line_number , i , end='')
            break
        print(line_number , i , end='')

