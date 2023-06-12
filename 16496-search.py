import functools

def compare(a, b):
    if a + b > b + a:
        return 1
    elif a + b < b + a:
        return -1
    else:
        return 0

def sort_numbers(numbers):
    str_numbers = numbers
    # 숫자들을 문자열로 변환합니다.
    # str_numbers = list(map(str, numbers))
    # 문자열로 변환한 숫자들을 정렬합니다.
    # str_numbers.sort(key=functools.cmp_to_key(compare))
    str_numbers.sort(key=lambda x: str(x)*100, reverse=True)
    
    return str_numbers


# def sort_numbers(numbers):
#     # 숫자들을 문자열로 변환합니다.
#     str_numbers = list(map(str, numbers))

#     # 'bubble sort' 알고리즘을 사용하여 숫자들을 정렬합니다.
#     for i in range(len(str_numbers)):
#         for j in range(len(str_numbers) - i - 1):
#             # 두 수를 이어붙였을 때 어느 쪽이 더 큰 수를 만드는지 비교합니다.
#             if str_numbers[j] + str_numbers[j+1] < str_numbers[j+1] + str_numbers[j]:
#                 # 만약 j번째 수와 j+1번째 수를 이어붙였을 때 j+1번째 수와 j번째 수를 이어붙인 것보다 작다면 두 수의 위치를 바꿉니다.
#                 str_numbers[j], str_numbers[j+1] = str_numbers[j+1], str_numbers[j]
                
#     return str_numbers

numbers = list(map(int, input().strip().split()))
print(sort_numbers(numbers))