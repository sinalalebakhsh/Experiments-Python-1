import requests



with open('urls.txt', 'a') as domain_site:
    while True:
        get_input = input('add your domain: ')
        if get_input == 'e':
            break
        elif get_input[:8] == 'https://':
            domain_site.write('\n'+get_input)
        
with open('urls.txt', 'r') as url_in_one_line:
    while True:
        one_url = url_in_one_line.readline().split()
        # print(one_url)
        try:
            if one_url[0] != '':
                link_line = requests.get(one_url[0])
                print(f'{one_url[0]} = {link_line.status_code}')
        except IndexError:
            break




#   https://www.google.com  
# https://www.salamatiyeshoma.com
# https://www.facebook.com
# https://www.yahoo.com
# https://www.moz.com





# http1 = requests.get('https://www.salamatiyeshoma.com')
# http2 = requests.get('https://salamatiyeshoma.com')
# http3 = requests.get('https://google.com')

# print(http1.content)
# print(http2.status_code)
# # print(http3.content)
# print(http3.status_code)
