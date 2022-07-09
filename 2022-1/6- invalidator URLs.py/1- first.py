import validators


with open('URL.txt') as f:
    lines = f.readlines()

for line in lines:
    url = line.strip()
    if validators.url(url):
        print('Valid URL: {}'.format(url))
    else:
        print('Invalid URL: {}'.format(url))
