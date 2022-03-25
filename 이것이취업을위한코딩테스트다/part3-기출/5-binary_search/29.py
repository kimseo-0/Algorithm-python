# 공유기 설치
# 무엇을 이분탐색 할것인가
# 문제에서 무엇을 이분탐색할지 잘 모르겠다면, 탐색을 하는 것 자체가 중요한 것이 아니라,
# 내가 찾고자 하는 값이 탐색을 했을 때, 정답인가 아닌가를 체크해야하는 문제일 확률이 높다
# 문제에서 요구하는 답을 기준(중간값)으로 탐색을 하면서 그 값이 정답인지 아닌지 확인하다자

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house_list = []
for i in range(N):
    house_list.append(int(input()))
house_list.sort()

max_distance = house_list[-1] - house_list[0]

start = 1
end = max_distance

while True:
    if start > end:
        break

    mid = (start + end) // 2

    count = 1
    prev = house_list[0]
    for i in range(1, N):
        if house_list[i] - prev >= mid:
            count += 1
            prev = house_list[i]

    if count < C:
        end = mid - 1
    else:
        max_distance = mid
        start = mid + 1

print(max_distance)

# # unsolved
# max_distance = (house_list[-1] - house_list[0]) // (C - 1)
#
# result_distance = house_list[-1] - house_list[0]
#
# start = 1
# end = N - 2
# start_house = house_list[start - 1]
# for i in range(2, C):
#     target = house_list[start - 1] + max_distance
#     min_distance = house_list[end + 1] - house_list[start - 1]
#     result_mid = 0
#     while start <= end:
#         mid = (start + end) // 2
#
#         if house_list[mid] == target:
#             result_mid = mid
#             break
#         elif house_list[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#
#         if min_distance > abs(target - house_list[mid]):
#             min_distance = abs(target - house_list[mid])
#             result_mid = mid
#
#     result_distance = min(result_distance, house_list[result_mid] - start_house)
#     start = result_mid + 1
#     end = N - 2
#     start_house = house_list[start]
#
#     if i == C - 1:
#         result_distance = min(result_distance, house_list[-1] - house_list[result_mid])
#
# print(result_distance)
