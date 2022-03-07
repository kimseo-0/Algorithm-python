import heapq
import sys
input = sys.stdin.readline

N = int(input())
DP = [1]

# solution 1
# num = 2
# while True:
#     if (num == 2) or (num == 3) or (num == 5):
#         DP.append(num)
#     else:
#         for i in range(len(DP) - 1, 1, -1):
#             if (num % DP[i] == 0) and ((num // DP[i]) == 2 or (num // DP[i]) == 3 or (num // DP[i] == 5)):
#                 DP.append(num)
#                 break
#     num += 1
#     if len(DP) == N:
#         break

# num = 2
# while True:
#     if num % 5 == 0:
#         if num // 5 in DP:
#             DP.append(num)
#     elif num % 3 == 0:
#         if num // 3 in DP:
#             DP.append(num)
#     elif num % 2 == 0:
#         if num // 2 in DP:
#             DP.append(num)
#
#     num += 1
#
#     if len(DP) == N:
#         break

# print(DP[N - 1])
# print(DP)

# solution 2
n = int(input())

q = []
heapq.heappush(q, 1)
for i in range(n):
    v = heapq.heappop(q)
    if v * 2 not in q:
        heapq.heappush(q, v * 2)
    if v * 3 not in q:
        heapq.heappush(q, v * 3)
    if v * 5 not in q:
        heapq.heappush(q, v * 5)
    if i == n - 1:
        print(v)



