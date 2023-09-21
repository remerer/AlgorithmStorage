import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n, k = map(int, input().strip().split())
array = []
q = deque()
for i in range(4):
    array.append(list(map(int, input().strip().split())))
array.sort(key=lambda x: x[1], reverse= True)
array.sort(key=lambda x: x[0])

valdp = [0 for i in range(k+1)]

for i in range(n):
    if array[i][1] > valdp[array[i][0]]:
        valdp[array[i][0]] = array[i][1]
        tmpw, tmpv = array.pop(i)
        q.append([tmpw, deepcopy(array)])
        array.insert(i,[tmpw,tmpv])

while(q):
    w, tmparray = q.pop()
    for i in range(len(tmparray)):
        if tmparray[i][1]+w > valdp[tmparray[i][0]+w]:
            tmpw, tmpv = tmparray.pop(i)
            q.append([tmpw+w, deepcopy(tmparray)])
            tmparray.insert(i-1,[tmpw,tmpv])

print(popdp)
print(valdp)
print(array)
print(q)