import sys
input = sys.stdin.readline

N = int(input())
value_list = []
for i in range(N):
    value_list.append(list(map(int, input().split())))

DP_R = [0] * N
DP_G = [0] * N
DP_B = [0] * N

DP_R[0] = value_list[0][0]
DP_G[0] = value_list[0][1]
DP_B[0] = value_list[0][2]

for i in range(1, N):
    DP_R[i] = min(value_list[i][0] + DP_G[i - 1], value_list[i][0] + DP_B[i - 1])
    DP_G[i] = min(value_list[i][1] + DP_B[i - 1], value_list[i][1] + DP_R[i - 1])
    DP_B[i] = min(value_list[i][2] + DP_R[i - 1], value_list[i][2] + DP_G[i - 1])

print(min(DP_R[N - 1], DP_G[N - 1], DP_B[N - 1]))

# https://www.acmicpc.net/problem/1149
