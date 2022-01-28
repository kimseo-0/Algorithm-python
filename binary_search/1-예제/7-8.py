import sys
input = sys.stdin.readline

def binary_search(array, target, start, end, result):

    if start > end:
        return result

    # 자를 위치
    mid = (start + end) // 2
    # 자른 떡을 길이 구하기
    sum_of_result = 0
    for element in array:
        if element > mid:
            sum_of_result += (element - mid)

    # 정확히 자른 떡의 길이가 원하는 떡의 양일 때
    if target == sum_of_result:
        return mid
    # 자른 떡의 양이 더 많을때, 오른쪽 탐색
    elif target < sum_of_result:
        # mid 값이 최대한 클 때를 찾고자 하므로 mid 의 값을 더 큰 값으로 갱신할 때 결과값을 저장한다.
        result = mid
        return binary_search(array, target, mid + 1, end, result)
    # 자른 떡의 양이 더 적을때, 왼쪽 탐색
    else:
        return binary_search(array, target, start, mid - 1, result)


N, M = map(int, input().split())
length_list = list(map(int, input().split()))
# length_list.sort()

# 재귀적 풀이
answer = binary_search(length_list, M, 1, max(length_list), 0)
print(answer)

# 위 문제는 start > end 까지 계산했을 때 정확한 M값이 나오지 않을 수 있다.
# 또한 mid 값이 최대한 클 때가 결과 값이 된다.
# 즉, 현재 얻을 수 있는 떡볶이의 양이 조건을 만족할 때만 결과 값이 될 수 있기 때문에
# 재귀적인 풀이보다는 반복문으로 풀이하는 것이 더 간단할 수 있다.

# 반복문 풀이
start = 0
end = max(length_list)
result = 0
while start <= end:
    mid = (start + end) // 2

    sum_of_result = 0
    for element in length_list:
        if element > mid:
            sum_of_result += (element - mid)

    if M == sum_of_result:
        result = mid
        break
    elif M < sum_of_result:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)