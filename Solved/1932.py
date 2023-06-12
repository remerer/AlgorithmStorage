import sys
input = sys.stdin.readline

#삼각형을만들고 똑같은 크기의 2차원 dp생성. dp len만큼 돌면서 해당 수가 가질수 잇는 최댓값 계산
#삼각형 꼭대기 / 바닥에서 시작하는건 상관 없음 (연산량, 결과 같음)
n = int(input().strip())
array = []
dp = []
for i in range(n):
    array.append(list(map(int, input().strip().split())))
for i in range(1, n+1):
    dp.append([-1 for _ in range(i)])
dp[0][0] = array[0][0]
for i in range(2, n+1):
    for j in range(i):
        if j == 0:
            dp[i-1][j] = array[i-1][j] + dp[i-2][j]
        elif j < i-1:
            dp[i-1][j] = array[i-1][j] + max(dp[i-2][j], dp[i-2][j-1])
        else:
            dp[i-1][j] = array[i-1][j] + dp[i-2][j-1]
print(max(dp[n-1]))