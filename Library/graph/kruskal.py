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


v, e = map(int, input().split())

parent_list = [0] * (v + 1)

for i in range(1, v + 1):
    parent_list[i] = i

edges = []
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

result = 0
for edge in edges:
    (cost, a, b) = edge

    if find_parent(a) != find_parent(b):
        union_parent(parent_list, a, b)
        result += cost

print(result)
