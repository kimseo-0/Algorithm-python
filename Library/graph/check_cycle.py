
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


v, e = map(int, input().split())    # 노드, 간선 갯수

parent_list = [0] * (v + 1)

# 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent_list[i] = i

cycle = False
for i in range(e):
    a, b = map(int, input().split())

    if find_parent(parent_list, a) == find_parent(parent_list, b):
        cycle = True
        break
    else:
        union_parent(parent_list, a, b)

print(cycle)
