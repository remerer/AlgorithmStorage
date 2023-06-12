import sys
input = sys.stdin.readline
from collections import deque

q = deque()
N, M = map(int, input().strip().split())
array = []
for _ in range(N):
    tmp = str(input().strip())
    tmparray =[]
    for i in range(M):
        tmparray.append(int(tmp[i]))
    array.append(tmparray)

q.append([0,0,1])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while(q):
    x, y, count = q.popleft()
    if x == N-1 and y == M-1:
        print(count)
        break
    for i in range(4):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < M:
            if array[x+dx[i]][y+dy[i]] == 1:
                array[x+dx[i]][y+dy[i]] = 0
                q.append([x+dx[i],y+dy[i],count+1])