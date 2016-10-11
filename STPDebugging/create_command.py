#!usr/bin/env python3
#-*- coding: utf-8 -*-

import struct 
import math
import binascii

s1 = math.sin(math.radians(145))
s2 = math.sin(math.radians(35))
s3 = math.sin(math.radians(225))
s4 = math.sin(math.radians(315))
c1 = math.cos(math.radians(145))
c2 = math.cos(math.radians(35))
c3 = math.cos(math.radians(225))
c4 = math.cos(math.radians(315))


l = 0.08    # m
radius = 53.75   # mm

STARTBYTE = b"\xFA"
STOPBYTE = b"\xFB"

crc8table = [0, 94, 188, 226, 97, 63, 221, 131, 194, 156, 126, 32, 163, 253, 31, 65,
            157, 195, 33, 127, 252, 162, 64, 30, 95, 1, 227, 189, 62, 96, 130, 220,
            35, 125, 159, 193, 66, 28, 254, 160, 225, 191, 93, 3, 128, 222, 60, 98,
            190, 224, 2, 92, 223, 129, 99, 61, 124, 34, 192, 158, 29, 67, 161, 255,
            70, 24, 250, 164, 39, 121, 155, 197, 132, 218, 56, 102, 229, 187, 89, 7,
            219, 133, 103, 57, 186, 228, 6, 88, 25, 71, 165, 251, 120, 38, 196, 154,
            101, 59, 217, 135, 4, 90, 184, 230, 167, 249, 27, 69, 198, 152, 122, 36,
            248, 166, 68, 26, 153, 199, 37, 123, 58, 100, 134, 216, 91, 5, 231, 185,
            140, 210, 48, 110, 237, 179, 81, 15, 78, 16, 242, 172, 47, 113, 147, 205,
            17, 79, 173, 243, 112, 46, 204, 146, 211, 141, 111, 49, 178, 236, 14, 80,
            175, 241, 19, 77, 206, 144, 114, 44, 109, 51, 209, 143, 12, 82, 176, 238,
            50, 108, 142, 208, 83, 13, 239, 177, 240, 174, 76, 18, 145, 207, 45, 115,
            202, 148, 118, 40, 171, 245, 23, 73, 8, 86, 180, 234, 105, 55, 213, 139,
            87, 9, 235, 181, 54, 104, 138, 212, 149, 203, 41, 119, 244, 170, 72, 22,
            233, 183, 85, 11, 136, 214, 52, 106, 43, 117, 151, 201, 74, 20, 246, 168,
            116, 42, 200, 150, 21, 75, 169, 247, 182, 232, 10, 84, 215, 137, 107, 53]

def _get_check_bytes(p_data):

    tmp=0
    for i in range(len(p_data)):
        tmp = crc8table[tmp^p_data[i]]

    low_check = (tmp>>4)& 0x0f
    high_check = tmp & 0x0f

    return low_check, high_check

def _convert_to_byte(data):
    tmp1 = hex(data)
    tmp2 = tmp1[2:len(tmp1)]
    if len(tmp2) % 2 == 1:
        tmp2 = '0' + tmp2

    return binascii.unhexlify(tmp2)

def create_command():
    #data = [1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
    #data = [1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    data = [4, 1, 35, 0]
    low_check, high_check = _get_check_bytes(data)

    packet = struct.pack("<BBBBBBBBBBBB", 1, 0, 1, 63, 1, 63, 1, 63, 1, 63, low_check, high_check)

    command = STARTBYTE + packet + STOPBYTE

    return command

def create_speed_command(x, y, theta, id, kick_speed):

    # Convert speed in x-y coordinate into speeds of four wheels 
    v1 = -s1 * x + c1 * y + l * theta
    v2 = -s2 * x + c2 * y + l * theta
    v3 = -s3 * x + c3 * y + l * theta
    v4 = -s4 * x + c4 * y + l * theta

    v1 = int(v1  * 100)
    v2 = int(v2  * 100)
    v3 = int(v3  * 100)
    v4 = int(v4  * 100)

    v1 = -v1
    v3 = -v3

    if v1 > 0:
        r1 = 0
    else:
        r1=1
        v1 = -v1

    if v2 > 0:
        r2 = 1
    else:
        r2=0
        v2 = -v2

    if v3 > 0:
        r3 = 0
    else:
        r3=1
        v3 = -v3

    if v4 > 0:
        r4 = 1
    else:
        r4=0
        v4 = -v4

    # Kick bit
    if kick_speed > 0:
        kick = 1
    else:
        kick = 0

    data = [id, kick, r1, v1, r2, v2, r3, v3, r4, v4]
     
    low_check, high_check = _get_check_bytes(data)

    v1_ = _convert_to_byte(v1)
    v2_ = _convert_to_byte(v2)
    v3_ = _convert_to_byte(v3)
    v4_ = _convert_to_byte(v4)

    id_ = _convert_to_byte(id)
    kick_ = _convert_to_byte(kick)
    r1_ = _convert_to_byte(r1)
    r2_ = _convert_to_byte(r2)
    r3_ = _convert_to_byte(r3)
    r4_ = _convert_to_byte(r4)


    low_check_ = _convert_to_byte(low_check)
    high_check_ = _convert_to_byte(high_check)

    #packet = struct.pack("<BBBBBBBBBBBB", id, kick, r1, v1, r2, v2, r3, v3, r4, v4, low_check, high_check)
    packet = id_ + kick_ + r1_ + v1_ + r2_ + v2_ + r3_ + v3_ + r4_ + v4_ + low_check_ + high_check_

    command = STARTBYTE + packet + STOPBYTE

    return command

if __name__ == '__main__':
    #print(create_speed_command(1, 1, 10, 1, 0))
    create_command()