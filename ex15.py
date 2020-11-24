#!/usr/bin/python

from sys import argv

script, filename = argv

txt = open(filename)

print(f'Here\' is your file {filename}:')
print(txt.readlines())

print('Type the filename again:')
file_again = input('>')

txt_again = open(file_again)

print(txt_again.read())
txt.close()