N = int(input())
num_list = list(map(int, input().split()))

DP_left = [1] * N
DP_right = [1] * N
result = 0
for i in range(N):
    for j in range(i):
        if num_list[j] < num_list[i]:
            DP_left[i] = max(DP_left[i], DP_left[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if num_list[j] < num_list[i]:
            DP_right[i] = max(DP_right[i], DP_right[j] + 1)

# print(DP_left)
# print(DP_right)

result = max([DP_right[i] + DP_left[i] for i in range(N)]) - 1
print(result)
