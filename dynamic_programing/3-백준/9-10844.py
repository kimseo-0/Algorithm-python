from copy import deepcopy

N = int(input())

DP = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
result = [0] * 10

for i in range(2, N + 1):
    for j in range(0, 10):
        if j == 0:
            result[j] = DP[1]
        elif j == 9:
            result[j] = DP[8]
        else:
            result[j] = DP[j - 1] + DP[j + 1]

    DP = deepcopy(result)

# print(DP)
print(sum(DP) % 1000000000)
