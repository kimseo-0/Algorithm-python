N = int(input())
DP = [0] * (N + 1)

DP[0] = 1
if N > 1:
    DP[2] = 3
for i in range(4, N + 1, 2):
    DP[i] = DP[i - 2] * 4 - DP[i - 4]
print(DP[N])