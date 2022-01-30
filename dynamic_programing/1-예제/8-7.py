N = int(input())

DP = [0] * (N + 1)

DP[1] = 1
DP[2] = 3

# print((2 * (N - 1) + 1) % 796796)

for i in range(3, N + 1):
    DP[i] = (DP[i - 2] * 2 + DP[i - 1]) % 769769

print(DP[N])
