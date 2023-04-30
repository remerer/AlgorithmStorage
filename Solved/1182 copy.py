N, S = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
picked = []
answer = 0

def backtrack(idx):
    global answer

    if len(picked) > 0 and sum(picked) == S:
        answer += 1
    #음수가 있어서 가지치기 안됨
    # elif sum(picked) > S:
    #     return 0

    for i in range(idx, N):
        picked.append(arr[i])
        backtrack(i + 1)
        picked.pop()


backtrack(0)
print(answer)