import requests

with open('urls.txt', 'a') as domain_site: #append
    while True:
        get_input = input('add your domain: ')
        if get_input == 'e':
            print('-'*20)
            break
        elif get_input[:8] == 'https://':
            domain_site.write('\n'+get_input)
        elif get_input[:7] == 'http://':
            domain_site.write('\n'+get_input)
        else:
            print('wrong link!')
            print('-'*20)

with open('urls.txt', 'r') as url_in_one_line: # read
    one_url = url_in_one_line.readline().split()
    empty_flag = 0
    while empty_flag == 0 :
        while True:
            one_url = url_in_one_line.readline().split()
            try:
                if one_url[0] != '': # https://google.com
                    try:
                        link_line = requests.get(one_url[0])
                        print(f'{one_url[0]} = {link_line.status_code}')
                        print('-'*20)
                    except:
                        print(f'{one_url[0]} = out of time for request')
                        print('-'*20)
                        break
            except IndexError:
                empty_flag = 1
                break


