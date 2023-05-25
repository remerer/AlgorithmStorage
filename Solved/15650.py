import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().strip().split())
array = [i for i in range(1,n+1)]
for index in combinations(array,m):
    for j in range(len(index)):
        print(index[j], end=' ')
    print()