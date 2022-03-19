# 카드 정렬하기
# 카드들 중 최소 값을 뽑는다.
# N이 십만이 넘기 때문에 NlogN 을 보장하는 코드가 필요하다.

import heapq
import sys
from queue import PriorityQueue

input = sys.stdin.readline
N = int(input())

result = 0
# solution 1
# card_num_list = PriorityQueue()
# for i in range(N):
#     card_num_list.put(int(input()))
#
# # N = 1일 때, 비교를 할 필요가 없다
# # if N == 1:
# #     result = card_num_list.get()
#
# while N > 1:
#     first = card_num_list.get()
#     second = card_num_list.get()
#     card_num_list.put(first + second)
#     result += (first + second)
#     N -= 1


result = 0
# solution2
card_num_list = []
for i in range(N):
    heapq.heappush(card_num_list, int(input()))

while len(card_num_list) > 1:
    first = heapq.heappop(card_num_list)
    second = heapq.heappop(card_num_list)
    temp = (first + second)
    result += temp
    heapq.heappush(card_num_list, temp)

print(result)
