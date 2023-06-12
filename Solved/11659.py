import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
Nlist = list(map(int, input().strip().split()))
dp = [0 for _ in range(N+1)]
dp[1] = Nlist[0]
for i in range(2,N+1):
    dp[i] = Nlist[i-1] + dp[i-1]
for _ in range(M):
    f,s = map(int, input().strip().split())
    print(dp[s]-dp[f-1])