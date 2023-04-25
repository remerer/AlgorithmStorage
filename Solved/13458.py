import sys
input = sys.stdin.readline
import math
import decimal

# 2초 / 512MB
# N개시험장, 각 시험장 응시자 수 Ai(list)
# 총감독관 B명감시, 부감독관 C명감시
# 총감독관1명, 부감독관 여러명
# 모든응시생 감시
# 각 시험장별 필요감독관 최소 수

N = int(input().strip())
students = list(map(int, input().strip().split()))
B, C = map(int, input().strip().split())
staff = 0

for i in range(N):
    students[i] -= B
    staff += 1
    if(students[i] > 0):
        staff += math.ceil(students[i]/C)
    
print(staff)
#왜틀림? 범위? 무제한이잖아
#부동소수점? decimal써도 안됨

#결과 : if(students[i] == 0): 아니고, >부호 써야함

