# import requests


from ntpath import join
from posixpath import split


with open('urls.txt', 'a') as domain_site:
    while True:
        get_input = input('add your domain: ')
        if get_input == 'exit':
            break
        domain_site.write('\n'+get_input)
    

    






# http1 = requests.get('https://www.salamatiyeshoma.com')
# http2 = requests.get('https://salamatiyeshoma.com')
# http3 = requests.get('https://google.com')

# print(http1.content)
# print(http2.status_code)
# # print(http3.content)
# print(http3.status_code)
