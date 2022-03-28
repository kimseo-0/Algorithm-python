# solved
N = int(input())
num_list = list(map(int, input().split()))

DP = [1] * N

for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            DP[i] = max(DP[i], DP[j] + 1)

# print(DP)
print(max(DP))

