import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('ru.wikipedia.org', 80))
content_items = [
    'GET / HTTP/1.1',
    'Most: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
content = '\n'.join(content_items)
print('--- HTTP MESSAGE ---')
print(content)
print('--- END OF MESSAGE ---')
sock.send(content.encode())
result = sock.recv(1024)
print(result.decode())
print('ok')