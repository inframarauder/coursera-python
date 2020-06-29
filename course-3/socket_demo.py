import socket


def write_to_file(data):
    f = open('files/socket_output.txt', 'a')
    f.write(data)
    f.close()


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    write_to_file(data.decode())

print('Done')
mysock.close()
