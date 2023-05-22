import sys
input = sys.stdin.readline

aptmap = []
aptarray = []
djcounter = 0
aptcount = 0

N = int(input().strip())
for _ in range(N):
    strtmp = input().strip()
    aptcount += strtmp.count("1")
    aptmap.append(list(map(int, strtmp)))

def aptcounter(x, y):
    global aptcounttmp
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    aptcounttmp += 1
    aptmap[x][y] = 0
    for k in range(4):
        if 0 <= x+dx[k] < N and 0 <= y+dy[k] < N:
            if aptmap[x+dx[k]][y+dy[k]] == 1:
                aptmap[x+dx[k]][y+dy[k]] = 0
                aptcounter(x+dx[k], y+dy[k])
    return aptcounttmp

for i in range(N):
    for j in range(N):
        if aptmap[i][j] == 1:
            djcounter += 1
            aptcounttmp = 0
            aptarray.append(aptcounter(i,j))
print(djcounter)
aptarray.sort()
for idx in aptarray:
    print(idx)
