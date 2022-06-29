def main():
    orginal_time = input('Enter time: ')
    converted_time = convert(orginal_time)
    if converted_time >= 7.0 and converted_time <= 8.0 :
        print('breakfast time')
    elif converted_time >= 12.0 and converted_time <= 13.0 :
        print('lunch time')
    elif converted_time >= 18.0 and converted_time <= 19.0 :
        print('dinner time')
    else:
        return


def convert(orginal_number):
    hours , minutes = orginal_number.split(':')
    hours = float(hours)
    minutes = float(minutes) * 60 / 3600
    return hours + minutes

main()
