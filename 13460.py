#2초 / 512MB

import sys
input = sys.stdin.readline
from collections import deque

#상하좌우로 기울일 수 있음
#4^10 = 2^20... 1048576...가능?
#BFS
#for문 네번...(최대숫자 제한 잘해야 함)

N, M = map(int, input().strip().split())
maplist = [list(input().strip()) for _ in range(N)]

RPos = [-1,-1]
BPos = [-1,-1]
OPos = [-1,-1]
GoalCount = -1
q = deque()

for i in range(N):
    for j in range(M):
        if(maplist[i][j] == "R"):
            RPos = [i, j]
            maplist[i][j] = '.'
        elif(maplist[i][j] == "B"):
            BPos = [i, j]
            maplist[i][j] = '.'
        elif(maplist[i][j] == "O"):
            OPos = [i, j]

def MovePosition(RP, BP, Dir, Cnt):
    if(Dir == 'U'):
        y, x = RP
        while(maplist[x][y-1] == ("#" or "B" or "O")):
            y = y-1
        RP = [x, y]
        y, x = BP
        while(maplist[x][y-1] == ("#" or "R" or "O")):
            y = y-1
        BP = [x, y]
    elif(Dir == 'D'):
        y, x = RP
        while(maplist[x][y+1] == ("#" or "B" or "O")):
            y = y+1
        RP = [x, y]
        y, x = BP
        while(maplist[x][y+1] == ("#" or "R" or "O")):
            y = y+1
        BP = [x, y]
    elif(Dir == 'L'):
        y, x = RP
        while(maplist[x-1][y] == ("#" or "B" or "O")):
            x = x-1
        RP = [x, y]
        y, x = BP
        while(maplist[x-1][y] == ("#" or "R" or "O")):
            x = x-1
        BP = [x, y]
    elif(Dir == 'R'):
        y, x = RP
        while(maplist[x+1][y] == ("#" or "B" or "O")):
            x = x+1
        RP = [x, y]
        y, x = BP
        while(maplist[x+1][y] == ("#" or "R" or "O")):
            x = x+1
        BP = [x, y]
    Cnt += 1
    return RP, BP, Cnt

print(GoalCount)