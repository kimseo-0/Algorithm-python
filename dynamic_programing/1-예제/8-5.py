N = int(input())
count = 0

# while N > 1:
#     count += 1
#     # print(count, N)
#     if N % 5 == 0:
#         N = (N // 5)
#         continue
#     elif N % 3 == 0:
#         N = (N // 3)
#         continue
#     elif (N - 1) % 5 == 0:      # 26
#         N = N - 1
#         continue
#     elif (N - 1) % 3 == 0:      # 22
#         if (N // 3) % 3 == 0:   # 28
#             N = N - 1
#             continue
#     elif N % 2 == 0:
#         N = N // 2
#         continue
#     else:
#         N = N - 1
# print(count)

DP = [0] * (N + 1)

for i in range(2, N + 1):
    DP[i] = DP[i-1] + 1
    if i % 2 == 0:
        DP[i] = min(DP[i // 2] + 1, DP[i])
    if i % 3 == 0:
        DP[i] = min(DP[i // 3] + 1, DP[i])
    if i % 5 == 0:
        DP[i] = min(DP[i // 5] + 1, DP[i])

print(DP[N])
