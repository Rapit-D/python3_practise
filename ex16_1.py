#!/usr/bin/python

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want to do that, press CTRL-C(^C).")
print("IF you want to do that, press RETURN.")

input("?")

print(f"opening {filename} ...")

fp = open(filename, 'w')

print(f"Erasing {filename}")
fp.truncate()

print(f"Let's write some content in {filename}.")
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

fp.write(f"{line1}\n{line2}\n{line3}\n")

print("We're going to close it.")
fp.close()
