import sys
input = sys.stdin.readline
from collections import deque
#dp + bfs

dp = [-1 for _ in range(100001)]
q = deque()
N, K = map(int, input().strip().split())
q.append([N, 0])
while(q):
    pos, cnt = q.popleft()
    if pos == K:
        print(cnt)
        break
    if pos*2 <= 100000 and (dp[pos*2] == -1 or dp[pos*2] > cnt+1):
        dp[pos*2] = cnt+1
        q.append([pos*2,cnt+1])
    if pos+1 <= 100000 and (dp[pos+1] == -1 or dp[pos+1] > cnt+1):
        dp[pos+1] = cnt+1
        q.append([pos+1, cnt+1])
    if 0 <= pos-1 and (dp[pos-1] == -1 or dp[pos-1] > cnt+1):
        dp[pos-1] = cnt+1
        q.append([pos-1, cnt+1])