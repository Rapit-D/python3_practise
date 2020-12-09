#!/usr/bin/python

from sys import argv
from os.path import exists

script, from_file, to_file = argv

infile = open(from_file)

if exists(to_file):
    print(f"The file {to_file} exists, please check it.")
else:
    print(f"The input file is {len(infile.read())} bytes long.")

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

fp = open(to_file, 'w')
fp.write(infile.read())
fp.close()
infile.close()
print("All done.")