import sys
input = sys.stdin.readline

dp = [-1 for _ in range(101)]
dp[1:11] = [1,1,1,2,2,3,4,5,7,9]

T = int(input().strip())

for _ in range(T):
    p = int(input().strip())
    if p <= 10:
        print(dp[p])
    else:
        for i in range(11,p+1):
            dp[i] = dp[i-2] + dp[i-3]
        print(dp[p])