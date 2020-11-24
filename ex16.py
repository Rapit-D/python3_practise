#!/usr/bin/python

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hin RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print(f"I'm going to write these to the {filename}")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()