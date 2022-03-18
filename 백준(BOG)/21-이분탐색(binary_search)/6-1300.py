import sys
input = sys.stdin.readline

# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25

N = int(input())
K = int(input())

# for K in range(1, (N * N) + 1):
#     start = 1
#     end = N * 2 - 1
#     num = 1
#     check_num = 1
#     while start <= end:
#         mid = (start + end) // 2
#
#         if mid <= N:
#             check = mid * (mid + 1) // 2
#         else:
#             check = (N * N) - ((N * 2 - 1 - mid) * (N * 2 - mid) // 2)
#
#         if check == K:
#             num = mid
#             check_num = check
#             break
#
#         if check < K:
#             start = mid + 1
#         else:
#             num = mid
#             check_num = check
#             end = mid - 1
#
#     # print(num)
#     # print(check_num)
#     if K == check_num:
#         if num % 2 != 0:
#             print(((num + 1) // 2) * ((num + 1) // 2))
#         else:
#             print(((num + 1) // 2 + 1) * ((num + 1) // 2))
#     else:
#         if num % 2 != 0:
#             print((((num + 1) // 2) - ((check_num - K + 1) // 2)) * (((num + 1) // 2) + ((check_num - K + 1) // 2)))
#         else:
#             print((((num + 1) // 2) - ((check_num - K) // 2)) * (((num + 1) // 2) + ((check_num - K) // 2) + 1))

start = 1
end = N * N

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in range(1, N + 1):
        count += min(mid // i, N)

    if count < K:
        start = mid + 1
    else:
        end = mid - 1

print(start)



