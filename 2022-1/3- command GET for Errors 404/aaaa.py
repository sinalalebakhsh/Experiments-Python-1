import requests

http1 = requests.get('https://www.salamatiyeshoma.com')
http2 = requests.get('https://salamatiyeshoma.com')
http3 = requests.get('https://google.com')

print(http1)
print(http2)
print(http3)

