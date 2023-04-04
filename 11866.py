import sys
input = sys.stdin.readline

#시간 2초 / 512MB
#n^2해도됨
#N명이 원으로 앉음
#k번째 사람 마다 제거
#linked list,

N, K = map(int, input().strip().split())

answerList = [1 for i in range(N+1)]
answerList[0] = 0
answer = []
people = [i for i in range(1,N+1)]

pt = -1
counter = 0
while(people):
    pt += 1
    counter += 1
    if(pt == len(people)):
        pt = 0
    if(counter == K):
        # print(pt)
        answer.append(people[pt])
        del(people[pt])
        pt -= 1
        counter = 0
    

print('<',end='')
print(*answer, sep=", ", end='')
print('>')

#1 2 3 4 6 7 8 9 10
#10 5
#counter = 5, pt = 4