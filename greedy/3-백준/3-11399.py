import sys
input = sys.stdin.readline

N = int(input())
time_list = list(map(int, input().split()))
time_list.sort()

min_sum = 0
for i in range(len(time_list)):
    min_sum += (N-i) * time_list[i]

print(min_sum)