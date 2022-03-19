# 안테나
# 08:11 - 08:25
# 일직선상에 여러채의 집
# 이 중 특정 위치의 집에 한개의 안테나 설치
# 안테나로부터 모든 집까지의 거리의 총합이 최소
# 동일한 위치에 여러개의 집이 존재하는 것이 가능


N = int(input())
house_list = list(map(int, input().split()))
house_list.sort()

# 초기 풀이로 시간초과가 발생한다
# for i in range(N):
#     result = sum(map(lambda x: abs(x - house_list[i]), house_list))
#     if (result < min_result) or (result == min_result and house_list[i] < answer):
#         answer = house_list[i]
#         min_result = result

# 중간값을 활용한 정답
# min_result = house_list[(N - 1) // 2]
# print(min_result)

# 중간값이 정답이라고 하기 전 생각한 풀이다.
# 중간값에 대한 풀이를 떠올린 과정에 대한 설명
# 및 위 풀이에 대한 이해를 돕기 위해 작성해보았다
# def binary_search(array, start, end):
#     if start > end:
#         return -1
#
#     mid = (start + end) // 2
#     mid_result = sum(map(lambda x: abs(x - house_list[mid]), house_list))
#     left_result = sum(map(lambda x: abs(x - house_list[(mid - 1) % N]), house_list))
#     right_result = sum(map(lambda x: abs(x - house_list[(mid + 1) % N]), house_list))
#
#     if mid_result <= left_result and mid_result <= right_result:
#         return mid
#     elif left_result < mid_result:
#         return binary_search(array, start, mid - 1)
#     elif right_result < mid_result:
#         return binary_search(array, mid + 1, end)
#
#
# result = binary_search(house_list, 0, N - 1)
#
# print(result)
# print(house_list[result])

# 4
# 5 1 7 9
# > 5
