N = int(input())
drink_list = [0] * (N + 1)
for i in range(1, N + 1):
    drink_list[i] = int(input())

DP = [0] * (N + 1)

if N > 0:
    DP[1] = drink_list[1]
if N > 1:
    DP[2] = drink_list[1] + drink_list[2]

for i in range(3, N + 1):
    DP[i] = max(DP[i - 1],
                DP[i-2] + drink_list[i],
                DP[i-3] + drink_list[i-1] + drink_list[i])

print(DP[N])
