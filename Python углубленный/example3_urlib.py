from urllib import request

response = request.urlopen('https://ru.wikipedia.org/?l')
print(response.headers.get('Content-type'))
print(response.getheader('Content-type'))