# 최대 병사의 수를 세는 것이 더 간단한다.
# DP 최대/최소를 구하는 문제에서
# 최소를 구하는 경우 전체에서 최대를 빼거나
# 최대를 구하는 경우 전체에서 최소를 빼는 것도 반드시 고려하자.

import sys
input = sys.stdin.readline

N = int(input())
power_list = list(map(int, input().split()))
# power_list.reverse()
DP = [1] * N

for i in range(1, N):
    for j in range(i):
        if power_list[i] < power_list[j]:
            DP[i] = max(DP[i], DP[j] + 1)

print(N - max(DP))
# print(power_list)
# print(DP)

# 7
# 15 11 4 8 5 2 4

# 9
# 15 11 5 4 3 8 6 2 1

# 6
# 2 1 2 1 2 1
