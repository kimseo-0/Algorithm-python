import sys
input = sys.stdin.readline


N, K = map(int, input().split())
DP = [[0] * (N + 1) for _ in range(K + 1)]

for k in range(K + 1):
    for n in range(N + 1):
        if n == 0 or k == 1:
            DP[k][n] = 1
        else:
            DP[k][n] = sum(DP[k - 1][:n + 1])

print(DP[K][N] % 1000000000)
