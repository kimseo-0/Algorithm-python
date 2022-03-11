from itertools import combinations
import sys
input = sys.stdin.readline

def calculate_city_distance(checks, houses):
    sum_of_distance = 0
    for (r1, c1) in houses:
        min_now = 10e9
        for (r2, c2) in checks:
            min_now = min(abs(r2 - r1) + abs(c2 - c1), min_now)
        sum_of_distance += min_now
    return sum_of_distance


N, M = map(int, input().split())
chicken_list = []
house_list = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 2:
            chicken_list.append((i, j))
        elif row[j] == 1:
            house_list.append((i, j))

result = 10e9
avail_chicken_list_combination = list(combinations(chicken_list, M))
for avail_chicken_list in avail_chicken_list_combination:
    result = min(calculate_city_distance(avail_chicken_list, house_list), result)

print(result)

