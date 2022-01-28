import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start >= end:
        return end

    # 자를 위치
    mid = (start + end) // 2

    # 자른 떡을 길이 구하기
    sum_of_result = 0
    for element in array:
        if element > mid:
            sum_of_result += (element - mid)

    # 정확히 자른 떡의 길이가 원하는 떡의 양일 때
    if M == sum_of_result:
        return mid
    # 자른 떡의 양이 더 많을때, 오른쪽 탐색
    elif M < sum_of_result:
        return binary_search(array, target, mid + 1, end)
    # 자른 떡의 양이 더 적을때, 왼족 탐색
    else:
        return binary_search(array, target, start, mid - 1)


N, M = map(int, input().split())
length_list = list(map(int, input().split()))
# length_list.sort()

result = binary_search(length_list, M, 1, max(length_list))
print(result)

# 위 문제는 start > end 까지 계산했을 때 정확한 M값이 나오지 않을 수 있다.
# 또한 mid 값이 최대한 클 때가 결과 값이 된다.
