# 계획에 있는 도시가 모두 같은 집합에 포함되는지 확인
import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent_list = [0] * (N + 1)
for i in range(N + 1):
    parent_list[i] = i

for row in range(1, N + 1):
    row_list = list(map(int, input().split()))
    for col in range(1, N + 1):
        if row > col:
            continue
        if row_list[col - 1] == 1:
            union_parent(parent_list, row, col)

# 크루스칼 알고리즘처럼 edge 리스트를 만들 필요가 없음
# print(edges)
# for edge in edges:
#     a, b = edge
#     union_parent(parent_list, a, b)

# print(parent_list)
result = True
plan_city = set(map(int, input().split()))
# print(plan_city)
compare_city = plan_city.pop()
for i in range(1, len(plan_city)):
    if parent_list[compare_city] != parent_list[plan_city.pop()]:
        result = False
        break

if result:
    print('YES')
else:
    print('NO')

# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3
# > YES

# 5 4
# 0 1 0 1 1
# 1 0 1 0 0
# 0 1 0 0 0
# 1 0 0 0 0
# 1 0 0 0 0
# 2 3 4 3
# > YES

# 5 4
# 0 1 0 1 1
# 1 0 0 1 0
# 0 0 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3
# > NO
