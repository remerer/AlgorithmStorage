import sys
input = sys.stdin.readline
from collections import deque
nowch = 100
movech = int(input().strip())
buttonlist = [0,1,2,3,4,5,6,7,8,9]
q = deque()
N = int(input().strip())
brokenlist = list(map(int, input().strip().split()))
for i in brokenlist:
    buttonlist.remove(i)

if(movech == 100):
    print(0)
else:
    count = 0
    q.append([0, 0])
    while(q):
        nowch, pressed = q.popleft()
        