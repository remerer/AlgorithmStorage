import sys
input = sys.stdin.readline
from collections import deque

q = deque()
N = int(input().strip())

minval = 10000000
maxval = 0
for _ in range(N):
    cmd = int(input().strip())
    if cmd == 0:
        try:
            print(q.popleft())
        except:
            print(0)
    elif q == deque():
        minval = cmd
        maxval = cmd
        q.append(cmd)
    elif cmd <= minval:
        q.appendleft(cmd)
        minval = cmd
    elif cmd >= maxval:
        q.append(cmd)
        maxval = cmd
    else:
        q.append(cmd)
        q= deque(sorted(q))