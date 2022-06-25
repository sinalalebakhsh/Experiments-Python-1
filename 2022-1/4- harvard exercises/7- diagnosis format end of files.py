user_input = input('Enter your name file: ') # file.jpg

if '.jpg' in user_input:
    print('image/jpeg')
elif '.pdf' in user_input:
    print('application/pdf')
elif '.gif' in user_input:
    print('image/gif')
elif '.jpeg' in user_input:
    print('image/jpeg')
elif '.png' in user_input:
    print('image/png')
elif '.txt' in user_input:
    print('text/plain')
elif '.zip' in user_input:
    print('application/zip')
elif '.PDF' in user_input:
    print('application/pdf')
else:
    print('application/octet-stream')
