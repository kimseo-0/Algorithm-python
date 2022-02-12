import sys
input = sys.stdin.readline

result = 0
num_list = list(map(int, list(input().strip())))
for num in num_list:
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
