import sys
input = sys.stdin.readline

n = int(input().strip())
k = int(input().strip())
array = list(map(int, input().strip().split()))
array = list(set(array))
array.sort()
dp = []
if len(array) != 1:
    answer = array[-1] - array[0]
    for i in range(len(array)):
        if i != 0:
            dp.append(array[i] - array[i-1])
    dp.sort()
    for _ in range(k-1):
        answer -= dp.pop()
else:
    answer = 0

print(answer)