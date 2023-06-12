import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
namelist = dict()
answerlist = []
for _ in range(N):
    namelist[str(input().strip())] = 1
for i in range(M):
    tmp = str(input().strip())
    try:
        if namelist[tmp] == 1:
            answerlist.append(tmp)
    except:
        pass
    
print(len(answerlist))
answerlist.sort()
for i in answerlist:
    print(i)