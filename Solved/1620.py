import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
numdict = dict()
namedict = dict()
for i in range(1,N+1):
    tmp = str(input().strip())
    namedict[tmp] = i
    numdict[str(i)] = tmp
for _ in range(M):
    tmp = str(input().strip())
    try:
        print(namedict[tmp])
    except:
        print(numdict[tmp])