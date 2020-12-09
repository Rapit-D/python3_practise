#!/usr/bin/python
import time

for i in '123456789':
    print(f'\b{i}', end='', flush=True)
    time.sleep(1)
    
# has problem on this script
