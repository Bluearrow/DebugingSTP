import socket
import sys

UDP_IP = "224.5.23.2"
UDP_PORT = 10006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024*1024)
    print("Receving: ", data)

def test_udp_1():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print("Failed to create socket.")
        sys.exit()

    host = "localhost"
    port = 8888

    while True:
        msg = raw_input("Input:")
        try:
            socket.sendto()

