from collections import deque


def BFS(graph, x, y):
    q = deque([(x, y)])

    while q:
        (x, y) = q.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


N, M = map(int, input().split())
maze_list = []
for i in range(N):
    maze_list.append(list(map(int, list(input()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

BFS(maze_list, 0, 0)

print(maze_list[N - 1][M - 1])