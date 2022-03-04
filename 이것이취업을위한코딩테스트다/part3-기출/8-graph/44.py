import sys
input = sys.stdin.readline
INF = 10e9

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


N = int(input())
position = [[i] for i in range(N)]
parents = [i for i in range(N)]

edges = []

for i in range(N):
    position[i].extend(list(map(int, input().split())))

# 아래와 같은 이유로 모든 가능한 엣지에 대해서 크루스칼 알고리즘을 수행할 수 없으므로
# 선택적으로 크루스칼 알고리즘을 수행하자

# 어떤 기준으로 선택을 할까?
# 최소 cost 가 되어야 하면, 모든 노드가 연결될 수 있어야 한다.

# 각각의 항목, x, y, z 에 대해서 정렬 했을 때 바로 옆 노드와 최소 거리가 된다.
# 해당 노드들은 모두 연결이 가능하다.

# x, y, z 만을 기준으로 했을 때, 최소 cost 가 나올 가능성이 있는 엣지들만 모아서
# 크루스칼 알고리즘을 수행한다.
for t in range(1, 4):
    position.sort(key=lambda el: el[t])
    for i in range(1, N):
        cost = min(abs(position[i][1] - position[i - 1][1]),
                   abs(position[i][2] - position[i - 1][2]),
                   abs(position[i][3] - position[i - 1][3]))
        edges.append((cost, position[i][0], position[i - 1][0]))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge

    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        result += cost

print(result)


# 아래의 방법을 사용해도 답을 낼 수 있지만,
# 메모리 초과 및 시간 초과가 발생한다.
# 시간의 경우,
# N = 십만 이기 떄문에,
# N = 십만인 경우 최소 N*logN 의 시간 복잡도로 해야한다.
# 메모리의 경우,
# N = 십만, N * (N - 1) 이 되면, 1억이 된다.
# 일반적으로 데이터가 천만 이하가 되야한다.

# for i in range(N):
#     position.append(list(map(int, input().split())))

# for i in range(N - 1):
#     min_cost = INF
#     # edge = (min_cost, 0, 0)
#     for j in range(i + 1, N):
#         cost = min(abs(position[i][0] - position[j][0]),
#                    abs(position[i][1] - position[j][1]),
#                    abs(position[i][2] - position[j][2]))
#         if cost < min_cost:
#             min_cost = cost
#     edges.append(min_cost)

# print(sum(edges))
