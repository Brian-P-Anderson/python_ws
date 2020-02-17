import socket

s = socket.socket()

port = 12345
s.bind(('', port))

s.listen(5)

while True:
  c, addr = s.accept()
  print ('Got connection from', addr)

  output = 'Thank you for connecting'
  c.sendall(output.encode('utf-8'))

  c.close()
