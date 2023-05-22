import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().strip().split()))
answer = 0
counter = 0
array.sort(reverse=True)
for i in range(len(array)):
    answer += array[i] * (i+1)
print(answer)