import sys
input = sys.stdin.readline

n = int(input().strip())
array = list(map(int, input().strip().split(" ")))
sortarray = list(sorted(set(array)))
numdict = dict()
for i in range(len(sortarray)):
    numdict[sortarray[i]] = i
for i in array:
    print(numdict[i], end=' ')