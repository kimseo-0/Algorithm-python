# 볼링공 고르기
# 목적 : 서로 다른 숫자의 볼링공을 선택하는 조합의 경우의 수
# 현재 상태 : 선택된적 없는 숫자의 볼링공에 대해서 > 자신과 다른 숫자를 가지 볼링공의 개수 + target
# 그리디 기준 : 같은 숫자의 볼링공 순서대로

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ball_weight_list = list(map(int, input().split()))
result = 0

# solution 1
# N*N/2
# for i in range(N):
#     for j in range(i + 1, N):
#         if ball_weight_list[i] != ball_weight_list[j]:
#             result += 1


# solution 2 : part1 + part2 [0, 0, 2, 2] > 1 * (2 + 2) + 2 * (2)
# part 1
count_list = [0] * (M + 1)
for i in range(N):
    count_list[ball_weight_list[i]] += 1

# part 2
# 해당 방법은 N(반복문) * N(sum 의 시간 복잡도)
# for i in range(N):
#     count_list[ball_weight_list[i]] -= 1
#     result += (sum(count_list) - count_list[ball_weight_list[i]])

# 이 방법은 M(반복문) * N(sum 의 시간 복잡도)
# for i in range(1, M):
#     count = count_list[i]
#     result += (sum(count_list[i + 1:]) * count)

for i in range(1, M + 1):
    N -= count_list[i]
    result += count_list[i] * N


# solution 3
# N*logN
# ball_weight_list.sort()
# count = 1
# for i in range(N - 1):
#     if ball_weight_list[i] == ball_weight_list[i + 1]:
#         count += 1
#     else:
#         result += (N - i - 1) * count
#
print(result)

# 8 5
# 1 5 4 3 2 4 5 2
# > 25
