import sys
input = sys.stdin.readline

N = int(input())
time_table = []  # [[T, P],[]]
for i in range(N):
    time_table.append(list(map(int, input().split())))

DP = [0] * (N + 1)
result = 0
for i in range(N - 1, -1, -1):
    time = time_table[i][0] + i
    if time <= N:
        DP[i] = max(result, time_table[i][1] + DP[time])
        result = max(result, DP[i])
    else:
        DP[i] = result

print(result)
