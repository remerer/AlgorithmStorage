import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().strip().split())
array = []
q = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
nottomato = 0
for i in range(N):
    redtemp = 0
    tmplist = list(map(int, input().strip().split(" ")))
    nottomato += tmplist.count(0)
    redtemp = tmplist.count(1)
    tmpy = 0
    for j in range(redtemp):
        if j ==0:
            tmpy = tmplist.index(1)
        else:
            tmpy = tmplist.index(1,tmpy+1)
        q.append([i,tmpy,0])
    array.append(tmplist)
countmax = 0
while(q and nottomato != 0):
    x, y, count = q.popleft()
    for i in range(4):
        if(0<= x+dx[i] < N) and (0 <= y+dy[i] < M):
            if(array[x+dx[i]][y+dy[i]] == 0):
                array[x+dx[i]][y+dy[i]] = 1
                nottomato -= 1
                countmax = max(countmax, count+1)
                q.append([x+dx[i],y+dy[i],count+1])

if(nottomato != 0):
    print(-1)
else:
    print(countmax)