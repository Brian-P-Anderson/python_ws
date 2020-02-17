import socket
s = socket.socket()

port = 12345

s.connect(('127.0.0.1', port))

while True:
  output = s.recv(1024)
  if len(output):
    print (s.recv(1024))
