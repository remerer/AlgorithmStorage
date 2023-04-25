import sys
input = sys.stdin.readline
from collections import deque


N = int(input().strip())
linelist = []
answerlist = deque()
linelength = 0

for _ in range(N):
    linelist.append(list(map(int, input().strip().split())))
linelist.sort()

for i in range(N):
    f, s = linelist[i]
    if(answerlist == deque()):
        answerlist.append(f)
        answerlist.append(s)
    else:
        if(f <= answerlist[-1]):
            answerlist[-1] = max(answerlist[-1], s)
        elif(f > answerlist[-1]):
            answerlist.append(f)
            answerlist.append(s)

while(answerlist):
    f = answerlist.popleft()
    s = answerlist.popleft()
    linelength += s-f

print(linelength)