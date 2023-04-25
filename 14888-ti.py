import sys
input = sys.stdin.readline
import itertools

# 2초 / 512MB
# 수열 N개
# 순서는 앞에서부터 연산
# N개수, N-1개 연산자 -> 결과가 최대, 최소
# +-*/

N = int(input().strip())
numList = list(map(int, input().strip().split()))
essentials = list(map(int, input().strip().split()))
essentialList = []
for i in range(4):
    for _ in range(essentials[i]):
        if(i == 0):
            essentialList.append('+')
        elif(i == 1):
            essentialList.append('-')
        elif(i == 2):
            essentialList.append('*')
        elif(i == 3):
            essentialList.append('/')

nPr = list(itertools.permutations(essentialList, N-1))
maxNum = -10_000_000_000
minNum = 10_000_000_000
for i in range(len(nPr)):
    SUM = numList[0]
    for j in range(N-1):
        if(nPr[i][j] == '+'):
            SUM = SUM + numList[j+1]
        elif(nPr[i][j] == '-'):
            SUM = SUM - numList[j+1]
        elif(nPr[i][j] == '*'):
            SUM = SUM * numList[j+1]
        elif(nPr[i][j] == '/'):
            if(SUM // numList[j+1] >= 0):
                SUM = SUM // numList[j+1]
            else:
                if(SUM < 0):
                    SUM = -SUM // numList[j+1]
                    SUM = -SUM
                else:
                    SUM = SUM // -numList[j+1]
                    SUM = -SUM
    maxNum = max(maxNum, SUM)
    minNum = min(minNum, SUM)
print(maxNum)
print(minNum)