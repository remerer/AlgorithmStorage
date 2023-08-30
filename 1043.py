import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
#사람수 N / 파티수 M
knows = list(map(int, input().strip().split()))
#사람수, 사람들이름 N개
knowslist = [False for _ in range(N)]
for i in range(1,len(knows)):
    knowslist[knows[i]-1] = True
parties = list()
for _ in range(M):
    parties.append(list(map(int, input().strip().split())))
flag = True

while(flag):
    flag = False
    for i in range(len(knowslist)):
        if knowslist[i] == True:
            for j in range(len(parties)):
                if i+1 in parties[j][1:]:
                    for k in range(1,len(parties[j])):
                        if knowslist[parties[j][k]-1] == False:
                            knowslist[parties[j][k]-1] = True
                            flag = True
answer = 0
for i in range(len(parties)):
    if knowslist[parties[i][1]-1] == False:
        answer += 1
print(answer)