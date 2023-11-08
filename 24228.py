import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

if k = 1:
    print(n+1)
else:
    print((n+1) + ((k-1)*2))