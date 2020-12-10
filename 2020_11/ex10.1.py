#!/usr/bin/python
import time

for i in range(9, -1, -1):
    print(f'\b{i}', end='', flush=True)
    time.sleep(1)
print("")

# 如果从10 以上的数字开始\b 退格一位，十位数会依旧显示。

for i in range(10, -1, -1):
    if abs(i) >= 9:
        print(f'\b\b{i}', end='', flush=True)
    elif abs(i) < 9:
        print(f'\b{i}', end='', flush=True)
    time.sleep(1)
print("")

# 还没有想明白10 到9 该怎么过渡