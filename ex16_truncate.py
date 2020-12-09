#!/usr/bin/python

from sys import argv

script, filename = argv

with open(filename, 'w') as fp:
    fp.truncate(5)
    fp.close()

## ex16.txt will be append with b'\x00\x00\x00\x00\x00' which ocupy 5 bytes in disk
## truncate will raise error 'io.UnsupportedOperation: File not open for writing' if the mode of open does set to 'w'