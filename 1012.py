import sys
input = sys.stdin.readline
from collections import deque

T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().strip().split())
    answer = 1
    array = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    for i in range(K):
        x, y = map(int, input().strip().split())
        array[y][x] = 1
    for i in range(M):
        for j in range(N):
            if(array[j][i] == 1):
                q.append([j, i])
                answer += 1
                while(q):
                    Y, X = q.pop()
                    array[Y][X] = answer
                    if(Y+1 <= N-1 and array[Y+1][X] == 1):
                        q.append([Y+1, X])
                    if(Y-1 >= 0 and array[Y-1][X] == 1):
                        q.append([Y-1, X])
                    if(X+1 <= M-1 and array[Y][X+1] == 1):
                        q.append([Y, X+1])
                    if(X-1 >= 0 and array[Y][X-1] == 1):
                        q.append([Y, X-1])  
    print(answer-1)