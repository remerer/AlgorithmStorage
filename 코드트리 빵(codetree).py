import sys
input = sys.stdin.readline
from collections import deque
#1초/80MB

N, M = map(int, input().strip().split())
#NxN의 격자
#M = N^2, 30중 작은수
#사람겹칠수 있고,
#n분에 n번째사람 spone, n+a분까지 a칸이동
#도착못하는 수는 없음
#↑, ←, →, ↓ 의 우선 순위

Map = []
Targetlen = 0
Target = deque()
searchMap = deque()
system = deque()

#region Timetick()
Time = 0
def Timetick():
    Time += 1
#endregion

#region Init Map, Target
for _ in range(N):
    Map.append(list(input().strip().split()))
for _ in range(M):
    x, y = map(int, input().strip().split())
    Target.append([x-1, y-1])
#endregion

def searchBase(Pos):
    TY, TX = Pos
    searchMap.append(Pos)
    while(searchMap):
        y, x = searchMap.popleft()
        if(y-1 >= 0):
            if(Map[y-1][x] == '1'):
                return [TY,TX],[y-1, x]
            else:
                searchMap.append([y-1, x])
        if(x-1 >= 0):
            if(Map[y][x-1] == '1'):
                return [TY,TX],[y, x-1]
            else:
                searchMap.append([y, x-1])
        if(x+1 < N):
            if(Map[y][x+1] == '1'):
                return [TY,TX],[y, x+1]
            else:
                searchMap.append([y, x+1])
        if(y+1 < N):
            if(Map[y+1][x] == '1'):
                return [TY,TX],[y+1, x]
            else:
                searchMap.append([y+1, x])

def MoveToTarget(TargetPos, NowPos, Time, ):
    searchMap.append(TargetPos, NowPos)

    while(searchMap):
        pass
        # if(searchMap)
        # else:
            # searchMap(TargetPos, NowPos, Time+1)
    #뭘넣어야 할까...
    #start pos, target pos, time? 넣고, deque append?
    #deque에서 

print(searchBase(Target.popleft()))

#1초동안 해야할 일 진행 후 time tick
while(Target and system):
    if(len(Target) != 0):
        [TY, TX], [SY, SX] = searchBase(Target.popleft())
        Map[SY][SX] = '2'
        system.append([SY, SX, Time])
    Timetick()

#pick basecamp
    #spone
#change map
#move to target(if reached == done)
#time tick
# while(Target):
#     if(Targetlen < Time)

# print(searchBase([2,3]))
# def MovePosition(nowPos, tarPos, time):
    #현재, 타겟, 나중위치
