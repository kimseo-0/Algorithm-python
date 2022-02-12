# https://www.acmicpc.net/problem/11690
# 1~N 까지 모든 자연수의 최소공배수
# unsolved

# 메모리 초과
# N = int(input())
#
# DP = [i for i in range(N + 1)]
#
# result = 1
# for n in range(2, N + 1):
#     is_available = False
#     for i in range(2, N + 1):
#         if DP[i] % n == 0:
#             is_available = True
#             DP[i] = DP[i] // n
#
#         if n == N:
#             result *= DP[i]
#
#     if is_available:
#         result *= n
#
# print(result % 2e32)

def LCM(a, b):
    min_num = min(a, b)
    max_num = max(a, b)
    result = 1
    for n in range(2, a):
        is_available = False
        if min_num % n == 0:
            is_available = True
            min_num //= n
        if max_num % n == 0:
            is_available = True
            max_num //= n
        if is_available:
            result *= n
    return int((result * min_num * max_num) % 2e32)

def LCM_N(n):
    result = 2
    for i in range(3, n + 1):
        result = LCM(result, i)
    return result


N = int(input())
print(LCM_N(N))
