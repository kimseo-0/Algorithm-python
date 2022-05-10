# 게임 맵 최단거리
# https://programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(graph, visited, N, M):
    queue = deque([(0, 0)])
    visited[0][0] = 1

    while queue:
        (x, y) = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue

            if graph[nx][ny] == 0:
                continue

            if visited[nx][ny] > -1:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1


def solution(maps):
    answer = 0

    n, m = len(maps), len(maps[0])
    visited = [[-1] * m for _ in range(n)]
    BFS(maps, visited, n, m)

    return visited[n - 1][m - 1]


solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
