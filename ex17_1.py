#!/usr/bin/python

from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file)

if exists(to_file):
    print(f"The input file is {len(in_file.read())} bytes long.")
    print("Ready, hit RETURN to continue, CTRL-C to abort.")
    input()
    
else:
    print(f"The file {to_file} exists, please check it.")

