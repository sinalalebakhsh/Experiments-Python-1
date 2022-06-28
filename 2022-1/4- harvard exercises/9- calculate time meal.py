
def main():
    orginal_time = input('Enter time: ')
    converted_time = convert(orginal_time)
    if converted_time >= 7.0 and converted_time <= 8.0 :
        print('breakfast time')
    else:
        return


def convert(orginal_number):
    hours , minutes = orginal_number.split(':')
    hours = float(hours)
    minutes = float(minutes) * 60 / 3600
    return hours + minutes

main()
