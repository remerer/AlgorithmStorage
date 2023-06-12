import sys
input = sys.stdin.readline
array =[]
N = int(input().strip())
for _ in range(N):
    array.append(list(map(int, input().strip().split())))
array.sort(key=lambda x:x[1])
array.sort(key=lambda x:x[0])
for i in range(N):
    print(array[i][0], array[i][1], sep=' ')
