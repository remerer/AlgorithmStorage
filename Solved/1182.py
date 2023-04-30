import sys
input = sys.stdin.readline
from itertools import combinations

N, S = map(int, input().strip().split())
Numlist = list(map(int, input().strip().split()))
answerlist = []
answer = 0
for i in range(N):
    answerlist += combinations(Numlist,i+1)
for j in answerlist:
    if(sum(j) == S):
        answer += 1
print(answer)

