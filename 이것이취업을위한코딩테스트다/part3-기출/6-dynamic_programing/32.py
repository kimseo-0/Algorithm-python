import sys
input = sys.stdin.readline


N = int(input())
num_list = []
for i in range(N):
    num_list.append(list(map(int, input().split())))

# for i in range(1, N):
#     for j in range(i + 1):
#         if j == 0:
#             num_list[i][j] = num_list[i - 1][j] + num_list[i][j]
#         elif j == i:
#             num_list[i][j] = num_list[i - 1][j - 1] + num_list[i][j]
#         else:
#             num_list[i][j] = max(num_list[i - 1][j], num_list[i - 1][j - 1]) + num_list[i][j]
#
# print(max(num_list[N - 1]))

# col 양쪽에 패딩 추가한 방법
# DP = [[0] * (N + 2) for _ in range(N)]
# DP[0][1] = num_list[0][0]
#
# for i in range(1, N):
#     for j in range(1, i + 2):
#         DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - 1]) + num_list[i][j - 1]
#
# print(max(DP[N - 1]))
