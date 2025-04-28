import serial
import sys
import time

device = serial.Serial(port = 'COM17', 
                       baudrate = 9600, 
                       bytesize = serial.EIGHTBITS,
                       parity = serial.PARITY_NONE, 
                       stopbits = serial.STOPBITS_ONE, 
                       timeout = 0.1)
carriage_return = bytes("\r", 'utf-8')
negative_acknowledge = ""
read_length = 64

ID = str(1) # 0 = valve 1, go to 2 and then 10
print(ID)

message = bytes(ID+'GO2\r', 'utf-8')	
device.write(message)
time.sleep(1)
response = device.read(read_length).split(carriage_return)
print(response)

message = bytes(ID+'GO10\r', 'utf-8')	
device.write(message)
time.sleep(1)
response = device.read(read_length).split(carriage_return)
print(response)

message = bytes(ID+'NP\r', 'utf-8')
device.write(message)
time.sleep(1)
response = device.read(read_length).split(carriage_return)
print(response)