import sys
input = sys.stdin.readline
from collections import deque
##역으로 커져가면 dp쓸수있지않나?

q = deque()
dp = [0 for _ in range(1000001)]
N = int(input().strip())
q.append([1, 0])
#이런식으로 풀면 안됨 (중복해서 보는 수가 너무많아짐)
while(q):
    n, c = q.popleft()
    dp[n] = c
    if(n*3<=N and dp[n*3] == 0):
        q.append(n*3, c+1)
    if(n*2<=N and dp[n*2] == 0):
        q.append(n*2, c+1)
    if(n+1<=N and dp[n+1] == 0):
        q.append(n+1, c+1)
print(dp[N])
#차라리 dp하나


# q.append([N, 0])

# while(q):
#     n, c = q.popleft()
#     if(n > 3):
#         if(n%3 == 0):
#             q.append([n/3, c+1])
#         if(n%2 == 0):
#             q.append([n/2, c+1])
#         q.append([n-1, c+1])
#     elif(n==3 or n==2):
#         print(c+1)
#         break
#     elif(n==1):
#         print(c)
#         break