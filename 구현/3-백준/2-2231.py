import sys
input = sys.stdin.readline
N = int(input())

result = 0
for i in range(N-(len(str(N)) * 9), N):
    sum_num = 0
    # (1) - 더 빠름
    num = i
    while num > 0:
        sum_num += num % 10
        num = num // 10
    # (2)
    # for num in str(i):
    #     sum_num += int(num)
    if N == (i + sum_num):
        result = i
        break

print(result)
