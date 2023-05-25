import sys
input = sys.stdin.readline
input()
#가장 긴 증가하는 부분수열
#입력받아서, 중복값제거하고 sort, len출력
#7
#60 10 20 10 30 20 50 일때, 5가아니라 4여야 함.
# 가장 작은값부터 시작해서도 안되고, 
#1000개밖에 안되면, N^2번 탐색가능
# 28 29 20 30

inputlist = list(map(int, input().split()))
dp = [0 for _ in range(len(inputlist))]
for i in range(1,len(inputlist)+1):
    for j in range(i-1,-1,-1):
        if inputlist[i-1] > inputlist[j]:
            dp[i-1] = max(dp[i-1], dp[j] +1)

print(max(dp)+1)

#재도전 후 통과!