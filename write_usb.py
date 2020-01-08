#!/usr/bin/python
import serial, time
from string import Template
from random import seed
from random import random

counter=0
seed(1)


ser = serial.Serial('/dev/ttyUSB1', 115200, 8, 'N', 1, timeout=1)
while True:
  randomWt = round(33 + 40 * random(), 2)
  ser.write(str.encode(f'Write counter: {counter}, Weight = {randomWt} \n'))
  time.sleep(5)
  counter += 1
