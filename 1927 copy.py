import sys
input = sys.stdin.readline
from collections import deque

array = deque()
N = int(input().strip())

for _ in range(N):
    cmd = int(input().strip())
    if cmd == 0:
        try:
            minval = min(array)
            array.remove(minval)
            print(minval)
        except:
            print(0)
    else:
        array.append(cmd)