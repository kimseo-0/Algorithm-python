# https://www.acmicpc.net/problem/13305

import sys
input = sys.stdin.readline
N = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = cost[0]
sum_cost = min_cost * distance[0]
for i in range(1, N - 1):
    if min_cost > cost[i] :
        min_cost = cost[i]
    sum_cost += min_cost * distance[i]

print(sum_cost)