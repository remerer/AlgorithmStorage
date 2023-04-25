import sys
input = sys.stdin.readline
flag = 1
while(flag != 0):
    tmp = str(input().strip())
    if(tmp == '0'):
        flag = 0
        break
    while(True):
        if(len(tmp)%2 == 1):
        #홀수일때
            firsttmp = tmp[:len(tmp)//2]
            secondtmp = tmp[len(tmp)//2+1:]
            secondtmp = secondtmp[::-1]
        else:
            firsttmp = tmp[:len(tmp)//2]
            secondtmp = tmp[len(tmp)//2:]
            secondtmp = secondtmp[::-1]
        if(firsttmp == secondtmp):
            print('yes')
            break
        else:
            print('no')
            break