# 2초 / 128MB
# 알고리즘 초당 약 1억 / 메모리크기는 ?
# N개가 순서가 바뀌면 안됨
# 강의수 100000, 각 길이 <10000
# 가능한 블루레이중 최소크기

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
lectureList = list(map(int, input().strip().split()))

print(lectureList)