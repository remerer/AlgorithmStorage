import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())
#1~n중에 m개고름

def printToN(start, end, m, array):
# s e까지 m개
# 부분문제
    #if 1~4까지2개씩?
    if len(array) == m:
        for i in range(len(array)):
            print(array[i], end=' ')
        print()
    elif len(array) < m:
        array.append(start)
        printToN(start,n,m,array)
        array.pop()
    if start+1 <= end:
        array.pop()
        array.append(start+1)
        printToN(start+1,n,m,array)


printToN(1,n,m,[1])
