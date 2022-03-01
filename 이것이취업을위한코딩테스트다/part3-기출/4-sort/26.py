import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())
card_num_list = PriorityQueue()
for i in range(N):
    card_num_list.put(int(input()))

result = 0

# N = 1일 때, 비교를 할 필요가 없다
# if N == 1:
#     result = card_num_list.get()

while N > 1:
    first = card_num_list.get()
    second = card_num_list.get()
    card_num_list.put(first + second)
    result += (first + second)
    N -= 1

print(result)
