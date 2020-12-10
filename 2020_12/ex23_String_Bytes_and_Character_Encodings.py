#!/usr/bin/python

import sys

script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
# 在main 函数内返回了一个main 函数
# 另类的循环，如果if 语句判断为True 则return main() 会回到main 函数的第一行重新运算

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding='utf-8')

main(languages, input_encoding, error)