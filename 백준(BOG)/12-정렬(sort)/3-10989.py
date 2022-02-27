import sys
input = sys.stdin.readline


count_list = [0] * 10001

N = int(input())
for i in range(N):
    count_list[int(input())] += 1

for i in range(1, 10001):
    for j in range(count_list[i]):
        print(i)
