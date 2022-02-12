def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def compare_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return True
    else:
        return False


N, M = map(int, input().split())
parent = [0] * (N + 1)
for i in range(N + 1):
    parent[i] = i

result = []
for i in range(M):
    op, a, b = map(int, input().split())

    if op == 0:
        union_parent(parent, a, b)
    else:
        if compare_parent(parent, a, b):
            result.append('YES')
        else:
            result.append('NO')

for i in result:
    print(i)
