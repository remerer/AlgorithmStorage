import sys
input = sys.stdin.readline

N = int(input().strip())
dp = [0 for _ in range(N+1)]
dp[0], dp[1], dp[2] = 1, 1, 2
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    for i in range(3,N+1):
        dp[i] = (dp[i-1] + dp[i-2])%10007
    print(dp[N]%10007)