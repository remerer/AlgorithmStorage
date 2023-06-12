import sys
input = sys.stdin.readline
#dp, bfs 문제(비용계산)
#직전집과 같지만 않으면 됨! * N번반복

N = int(input().strip())
dp = [[1001,1001,1001] for _ in range(1001)]
dp[0] = [0,0,0]
array = []
array.append([0,0,0])
for i in range(1,N+1):
    a, b, c = map(int, input().strip().split())
    dp[i][0] = min(a+dp[i-1][1], a+dp[i-1][2])
    dp[i][1] = min(b+dp[i-1][0], b+dp[i-1][2])
    dp[i][2] = min(c+dp[i-1][0], c+dp[i-1][1])
print(min(dp[N]))

#   array       dp
#   [10,20,1]   [10, 20, 1]
#   [10,20,1]   [11, 21, 11]
