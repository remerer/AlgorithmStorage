import sys
input = sys.stdin.readline
from collections import deque

# dfs
# 사다리꼴모양 범위에서 4개의 값을더했을 때의 최댓값
# 시간제한 2초
# 메모리 512MB
# N, M <500
# 500^2*4! = 25000 * 24 = 600,000
# N^2이지만, 600000회 == 1초이내

#현재위치, 스코어, 방향, 덧셈카운트(3회까지)
    
N, M = map(int, input().strip().split())
array = []
maxScore = [[-1 for _ in range(M+2)] for _ in range(N+2)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()



# -1로 네방향 Padding
array.append([-1 for _ in range(N+2)])
for _ in range(N):
    array.append([-1, *list(map(int, input().strip().split())), -1])
array.append([-1 for _ in range(N+2)])

for i in range(1, N+1):
    for j in range(1, M+1):
        #각자리에서 최댓값
        q.append([i,j,array[i][j],0,0])
        while(q):
            x, y, score, dir, count = q.popleft()
            if(count < 4):
                for k in range(4):
                    if(array[i+dx[k]][j+dx[k]] != -1 and k+1 != dir):
                        q.append([x+dx[k],y+dx[k], score+array[i+dx[k]][j+dx[k]],k+1,count+1])
            else:
                maxScore[i][j] = max(maxScore[i][j], score)

print(max(maxScore))

        
