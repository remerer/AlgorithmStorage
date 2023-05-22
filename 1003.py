import sys
input = sys.stdin.readline
from collections import deque

d = [0 for _ in range(41)]

d[1] = 1
d[2] = 1
n = int(input().strip())

def fibo(x):
    if d[x] == 0:
        if x == 1 and x == 2 :
            return 1
        else:
            d[x] = fibo(x-1)+fibo(x-2)
            return d[x]
    else:
        return d[x]

for _ in range(n):
    innum = int(input().strip())
    if innum == 0:
        print("1 0")
    elif innum == 1:
        print("0 1")
    else:
        print(fibo(innum-1), fibo(innum),sep=' ')