import sys
input = sys.stdin.readline
from collections import deque

T = int(input().strip())
for _ in range(T):
    answer = []
    p = deque(list(input().strip()))
    n = int(input().strip())
    flag = True

    try:
        array = deque(map(int, input().strip('[]\n').split(',')))
    except:
        array = []
    while(p!=deque([])):
        try:
            tmp = p.popleft()
            if(p != deque([])):
                if(tmp == 'R' and p[0] == 'R'):
                    p.popleft()
                    continue
            if(tmp == 'R'):
                if(flag==True):
                    flag = False
                else:
                    flag = True
            elif(tmp == 'D'):
                if(flag==True):
                    array.popleft()
                else:
                    array.pop()
        except:
            answer = 'error'
            
    if(answer != 'error'):
        if(flag==False):
            array.reverse()
        print('[',end='')
        for i in range(len(array)):
            print(array[i],end='')
            if(i != len(array)-1):
                print(',',end='')
        print(']')
    else:
        print(answer)