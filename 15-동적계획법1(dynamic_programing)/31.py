# 맨 첫번째 줄 어느 행에서든 출발 가능
# m번 이동 가능
# 이동 방향 : 오른쪽 위, 오른족, 오른쪽 아래, (아래?)
# 최대 크기(cost)

import sys
input = sys.stdin.readline

T = int(input())
result = []
for i in range(T):
    N, M = map(int, input().split())
    gold_list = list(map(int, input().split()))
    DP = [[0] * (N + 2) for _ in range(M + 1)]

    for j in range(1, M + 1):   # 1 2 3 4
        for k in range(1, N + 1):   # 1 2 3
            DP[j][k] = gold_list[(k - 1) * M + j - 1]

    for j in range(2, M + 1):
        for k in range(1, N + 1):
            DP[j][k] = max(DP[j - 1][k - 1], DP[j - 1][k], DP[j - 1][k + 1]) + DP[j][k]

    print(DP)
    result.append(max(DP[M]))

for i in result:
    print(i)

# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
