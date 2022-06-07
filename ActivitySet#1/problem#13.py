# Network Programming
# https://www.py4e.com/lessons/network

'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.com', 80))
cmd = 'GET https://www.py4e.com/lessons/network HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

'''

