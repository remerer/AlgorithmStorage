import sys
input = sys.stdin.readline
# N < 500,000

from collections import deque

N = int(input().strip())
cards = deque(i for i in range(1,N+1))

while(len(cards)!=1):
    cards.popleft()
    cards.append(cards.popleft())
    
print(cards[0])

###수학적으로 풀이 가능! (2^n = 2^n값, 2^n+1 = 2, 2^n +2 = 4...2^2n = 2^2n)