# import sys
# input = sys.stdin.readline
#
# N = int(input())
# time_list = list(map(int, input().split()))
# time_list.sort()
#
# min_sum = 0
# for i in range(len(time_list)):
#     min_sum += (N-i) * time_list[i]
#
# print(min_sum)

# 2차 풀이
import sys
input = sys.stdin.readline

N = int(input())
time_list = list(map(int, input().split()))
time_list.sort()

prev_time = time_list[0]
min_sum = prev_time
for i in range(1, N):
    prev_time += time_list[i]
    min_sum += prev_time

print(min_sum)
