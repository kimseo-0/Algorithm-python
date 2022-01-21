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


def BFS(graph, v, visited):
    queue = deque([v])

    if graph[v[0]][v[1]] == 1 or visited[v[0]][v[1]] == 1:
        visited[v[0]][v[1]] = 1
        return False

    visited[v[0]][v[1]] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        v = queue.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return True


N, M = map(int, input().split())
ice_list = []
for i in range(N):
    ice_list.append(list(map(int, list(input()))))

visited_list = [[0] * M for _ in range(N)]

count = 0
for i in range(N):
    for j in range(M):
        result = BFS(ice_list, (i, j), visited_list)
        if result:
            count += 1

print(count)

# 4 5
# 00110
# 00011
# 11111
# 00000
