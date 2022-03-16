# 모험가 길드
# 그리디 기준 : 공포도가 낮은 순서대로

N = int(input())
fear_list = list(map(int, input().split()))

fear_list.sort()

count_friend = 0
count_team = 0
for i in fear_list:
    count_friend += 1
    if count_friend >= i:
        count_team += 1
        count_friend = 0

print(count_team)

# 비효율적인 풀이
# i = 0
# count = 0
# left = 0
# while i < N:
#     if i + fear_list[i] - 1 < N and fear_list[i + fear_list[i] - 1] <= fear_list[i]:
#         count += 1
#         i += fear_list[i]
#     else:
#         left += 1
#         if fear_list[i] <= left:
#             left -= fear_list[i]
#             count += 1
#         i += 1
# print(count)

# 잘못되었음을 감지했을 때는 문제를 다시 읽자
