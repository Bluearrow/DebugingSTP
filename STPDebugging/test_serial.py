#-*- coding: utf-8 -*-

# FA010101000100010001000505FB
# FA010001630163016301630007FB


import serial
import serial.tools.list_ports
import struct
import time
import binascii

# List avaiable port with python
def list_ports():
    ports = list(serial.tools.list_ports.comports())
    port = list(ports[0])[0]

    return port


STARTBYTE = b"\xFA"
STOPBYTE = b"\xFB"
packet = struct.pack("<BBBBBBBBBBBB", 1, 0, 1, 63, 1, 63, 1, 63, 1, 63, 0, 7)
packet1 = struct.pack("<BBBBBBBBBBBB", 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 5, 5)

aa = b"\xFA\x01\x00\x01\x63\x01\x63\x01\x63\x01\x63\x00\x07\xFB"
bb = b"\xFA\x01\x01\x01\x00\x01\x00\x01\x00\x01\x00\x05\x05\xFB"
cc = b"\xFA\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\0x0c\0x0c\xfb"

a = STARTBYTE + packet + STOPBYTE
b = STARTBYTE + packet1 + STOPBYTE
print(a)

port = 'COM5'
rate = 115200
ser = serial.Serial(port, rate)


n = ser.write(a)
print(n)

ss = ser.read(n)
print(ss)


i = 0
while True:
    print('Start sending...')
    if i % 2 == 0:
        n = ser.write(cc)
        time.sleep(1)
    else:
        n = ser.write(bb)
        time.sleep(5)
    print('Start receiving...')
    ss = ser.read(8)
    print('Stop receiving.')
    i += 1
    print(i)
    print(ss)

ser.close()
