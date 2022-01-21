from collections import deque


def DFS(graph, v):
    if v[0] <= -1 or v[0] >= N or v[1] <= -1 or v[1] >= M:
        return False
    if graph[v[0]][v[1]] == 1:
        return False
    else:
        print(v)
        graph[v[0]][v[1]] = 1
        DFS(graph, (v[0] + 1, v[1]))
        DFS(graph, (v[0], v[1] + 1))
        DFS(graph, (v[0] - 1, v[1]))
        DFS(graph, (v[0], v[1] - 1))

        return True

def BFS(graph, v):
    queue = deque([v])

    graph[v[0]][v[1]] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if graph[v[0]][v[1]] == 0:
                queue.append(i)
                graph[v[0]][v[1]] = 1


N, M = map(int, input().split())
ice_list = []
for i in range(N):
    ice_list.append(list(map(int, input())))

visited_list = [[False] * M] * N

count = 0
for i in range(N):
    for j in range(M):
        result = DFS(ice_list, (i, j))
        if result:
            count += 1

print(count)