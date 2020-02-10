#!/usr/bin/python
import serial, time
from string import Template
from random import seed
from random import random

counter=0
seed(1)

def my_function(rWt):
  output = ''
  rangePad = int(round(4 * random(), 0))
  for x in range(6 + rangePad):
#    output = output + str.encode(f'Z1G        0.00lb \r\n')
    output = output + str(f'Z1G        0.00lb \r\n')
  rangePad = int(round(4 * random(), 0))
  for x in range(6 + rangePad):
    incrWt = rWt / (6 + rangePad)
    loopWt = round(incrWt * x, 2)
#    output = output + str.encode(f' 1GM      {loopWt}lb \r\n')
    output = output + str(f' 1GM      {loopWt}lb \r\n')
  for x in range(6 + rangePad):
#    output = output + str.encode(f' 1G        {rWt}lb \r\n')
    output = output + str(f' 1G        {rWt}lb \r\n')
  for x in range(6 + rangePad):
    incrWt = rWt / (6 + rangePad)
    loopWt = round(rWt - incrWt * x, 2)
#    output = output + str.encode(f' 1GM      {loopWt}lb \r\n')
    output = output + str(f' 1GM      {loopWt}lb \r\n')
  for x in range(6 + rangePad):
#    output = output + str.encode(f'Z1G        0.00lb \r\n')
    output = output + str(f'Z1G        0.00lb \r\n')
  return output

# ser = serial.Serial('/dev/ttyUSB1', 115200, 8, 'N', 1, timeout=1)
while True:
  randomWt = round(56 + 7 * random(), 2)
#  ser.write(my_function(randomWt))
  print(my_function(randomWt))
  time.sleep(.05)
  counter += 1
