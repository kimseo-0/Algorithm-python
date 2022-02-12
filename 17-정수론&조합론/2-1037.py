# N의 약수들로 N 구하기
import sys
input = sys.stdin.readline


# N = int(input())
# factor_list = list(map(int, input().split()))
# factor_list.sort()
# DP = [factor for factor in factor_list]
#
# result = 1
# for i in range(N):
#     flag = False
#     n = DP[i]
#     for j in range(N):
#         if DP[j] % n == 0:
#             DP[j] //= n
#             flag = True
#     if flag:
#         result *= n
#
# if result in factor_list:
#     result *= factor_list[0]
#
# print(result)

# N = int(input())
# factor_list = list(map(int, input().split()))
# print(min(factor_list) * max(factor_list))

N = int(input())
factor_list = list(map(int, input().split()))
factor_list.sort()
print(factor_list[0] * factor_list[-1])
