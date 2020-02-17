#!/usr/bin/python
import serial, time
import socket
from string import Template
from random import seed
from random import random

s = socket.socket()

port = 12345
s.bind(('', port))

s.listen(5)

counter=0
seed(1)

def my_function(rWt):
  output = ''
  rangePad = int(round(4 * random(), 0))
  for x in range(6 + rangePad):
    output = output + str(f'Z1G        0.00lb \r\n')
  rangePad = int(round(4 * random(), 0))
  for x in range(6 + rangePad):
    incrWt = rWt / (6 + rangePad)
    loopWt = round(incrWt * x, 2)
    output = output + str(f' 1GM      {loopWt}lb \r\n')
  for x in range(6 + rangePad):
    output = output + str(f' 1G        {rWt}lb \r\n')
  for x in range(6 + rangePad):
    incrWt = rWt / (6 + rangePad)
    loopWt = round(rWt - incrWt * x, 2)
    output = output + str(f' 1GM      {loopWt}lb \r\n')
  for x in range(6 + rangePad):
    output = output + str(f'Z1G        0.00lb \r\n')
  print('Through my_function {output}')
  return str.encode(output)

# ser = serial.Serial('/dev/ttyUSB1', 115200, 8, 'N', 1, timeout=1)
while True:
  c, addr = s.accept()
  print ('Got connection from', addr)

  randomWt = round(56 + 7 * random(), 2)
#  ser.write(my_function(randomWt))

  c.sendall(my_function(randomWt))
  time.sleep(.05)
  counter += 1
  c.close()
