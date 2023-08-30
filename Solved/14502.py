import sys
input = sys.stdin.readline
from itertools  import combinations 
from collections import deque
from copy import deepcopy

n, m = map(int, input().strip().split())
array = []
emptylist = []
workq = deque()
viruslist = deque()
zerocount = 0
answer = 0
dx = [1, -1, 0,0]
dy = [0,0, 1,-1]

for i in range(n):
    tmplist = list(map(int, input().strip().split()))
    array.append(tmplist)
    for j in range(m):
        if tmplist[j] == 0:
            emptylist.append([i,j])
        elif tmplist[j] == 2:
            viruslist.append([i,j])
    zerocount += tmplist.count(0)
combi = list(combinations(emptylist,3))
#전수조사 = 최대 64칸 => 64*63*62만큼 벽갯수 가능

for i in range(len(combi)):
    workq.append([combi[i], deepcopy(array), deepcopy(viruslist), deepcopy(zerocount)])

while(workq):
    ([x1, y1], [x2, y2], [x3, y3]), tmparray, tmpvirus, tmpzero = workq.popleft()
    tmparray[x1][y1] = 1
    tmparray[x2][y2] = 1
    tmparray[x3][y3] = 1
    tmpzero -= 3

    while(tmpvirus):
        x, y = tmpvirus.popleft()
        for i in range(4):
            if 0 <= x+dx[i] < n and 0 <= y+dy[i] < m:
                if tmparray[x+dx[i]][y+dy[i]] == 0:
                    tmparray[x+dx[i]][y+dy[i]] = 2
                    tmpzero -= 1
                    tmpvirus.append([x+dx[i],y+dy[i]])
            if tmpzero <= answer:
                break
    answer = max(answer, tmpzero)
print(answer)