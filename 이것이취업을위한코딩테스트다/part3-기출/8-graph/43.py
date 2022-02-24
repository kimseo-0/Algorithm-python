def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N, M = map(int, input().split())

parents = [i for i in range(N)]
edges = []
result = 0
for i in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    # result += cost

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        # result -= cost
    else:
        result += cost

print(result)

# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11
# > 51
