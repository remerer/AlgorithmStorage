import sys
input = sys.stdin.readline

N = int(input().strip())
dp = [99999 for _ in range(N+1)]
dp[3] = 1
if(N>=5):
    dp[5] = 1
for i in range(3,N+1):
    if(i>=5 and dp[i-3] != -1):
        dp[i] = min(dp[i-3] + 1, dp[i])
    if(i>=5 and dp[i-5] != -1):
        dp[i] = min(dp[i-5] + 1, dp[i])
    print(i, dp[i], dp[i-3], dp[i-5])

if(dp[N] == 99999):
    print(-1)
else:
    print(dp[N])