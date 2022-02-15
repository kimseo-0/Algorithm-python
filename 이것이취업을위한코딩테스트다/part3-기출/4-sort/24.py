# 08:11 - 08:25
# 일직선상에 여러채의 집
# 이 중 특정 위치의 집에 한개의 안테나 설치
# 안테나로부터 모든 집까지의 거리의 총합이 최소
# 동일한 위치에 여러개의 집이 존재하는 것이 가능


N = int(input())
house_list = list(map(int, input().split()))
house_list.sort()

min_result = house_list[(N - 1) // 2]

print(min_result)


# for i in range(N):
#     result = sum(map(lambda x: abs(x - house_list[i]), house_list))
#     if (result < min_result) or (result == min_result and house_list[i] < answer):
#         answer = house_list[i]
#         min_result = result

# 4
# 5 1 7 9
# > 5
