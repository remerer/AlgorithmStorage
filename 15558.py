import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    a, b = map(int, input().strip().split())
    print(a+b)