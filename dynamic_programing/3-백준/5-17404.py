import sys
input = sys.stdin.readline

N = int(input())
value_list = []
for i in range(N):
    value_list.append(list(map(int, input().split())))

DP_R = [0] * N
DP_G = [0] * N
DP_B = [0] * N

DP_R[1] = value_list[1][0]
DP_G[1] = value_list[1][1]
DP_B[1] = value_list[1][2]

pre_start_R = 0
pre_start_G = 1
pre_start_B = 2
start_R = 0
start_G = 1
start_B = 2

for i in range(2, N):
    if value_list[i][0] + DP_G[i - 1] <= value_list[i][0] + DP_B[i - 1]:
        DP_R[i] = value_list[i][0] + DP_G[i - 1]
        start_R = pre_start_G
    else:
        DP_R[i] = value_list[i][0] + DP_B[i - 1]
        start_R = pre_start_B
    if value_list[i][1] + DP_B[i - 1] <= value_list[i][1] + DP_R[i - 1]:
        DP_G[i] = value_list[i][1] + DP_B[i - 1]
        start_G = pre_start_B
    else:
        DP_G[i] = value_list[i][1] + DP_R[i - 1]
        start_G = pre_start_R
    if value_list[i][2] + DP_R[i - 1] <= value_list[i][2] + DP_G[i - 1]:
        DP_B[i] = value_list[i][2] + DP_R[i - 1]
        start_B = pre_start_R
    else:
        DP_B[i] = value_list[i][2] + DP_G[i - 1]
        start_B = pre_start_G

    pre_start_R = start_R
    pre_start_G = start_G
    pre_start_B = start_B

result = []

if start_R == 0:
    result.append(DP_R[N - 1] + value_list[0][1])
    result.append(DP_R[N - 1] + value_list[0][2])
elif start_R == 1:
    result.append(DP_R[N - 1] + value_list[0][2])
else:
    result.append(DP_R[N - 1] + value_list[0][1])

if start_G == 1:
    result.append(DP_G[N - 1] + value_list[0][0])
    result.append(DP_G[N - 1] + value_list[0][2])
elif start_G == 0:
    result.append(DP_G[N - 1] + value_list[0][2])
else:
    result.append(DP_G[N - 1] + value_list[0][0])

if start_B == 2:
    result.append(DP_B[N - 1] + value_list[0][0])
    result.append(DP_B[N - 1] + value_list[0][1])
elif start_B == 1:
    result.append(DP_B[N - 1] + value_list[0][0])
else:
    result.append(DP_B[N - 1] + value_list[0][1])

print(DP_R)
print(DP_G)
print(DP_B)

print(min(result))

# https://www.acmicpc.net/problem/1149 와 연결되는 문제
# https://www.acmicpc.net/problem/17404