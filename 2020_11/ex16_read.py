#!/usr/bin/python

from sys import argv

script, filename = argv

print(f"We're going to check the {filename}")
fp = open(filename, 'r')
print(fp.read())
fp.close()