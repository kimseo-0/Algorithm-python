N = int(input())
stair_list = [0]
for i in range(N):
    stair_list.append(int(input()))

DP = [0] * (N + 1)
if N >= 1:
    DP[1] = stair_list[1]
if N >= 2:
    DP[2] = stair_list[1] + stair_list[2]
if N >= 3:
    for i in range(3, N + 1):
        DP[i] = max(DP[i - 3] + stair_list[i - 1], DP[i - 2]) + stair_list[i]

print(DP[N])
