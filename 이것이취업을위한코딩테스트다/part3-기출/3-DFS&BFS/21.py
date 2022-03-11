import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(graph, x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    country_list = [(x, y)]
    sum_of_people = graph[x][y]
    while q:
        (x, y) = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
                continue
            if visited[nx][ny] == 1:
                continue
            if (abs(graph[nx][ny] - graph[x][y]) < L) or (R < abs(graph[nx][ny] - graph[x][y])):
                continue

            visited[nx][ny] = 1
            country_list.append((nx, ny))
            sum_of_people += graph[nx][ny]
            q.append((nx, ny))

    if len(country_list) > 1:
        new_num = sum_of_people // len(country_list)
        for (x, y) in country_list:
            graph[x][y] = new_num
        return True
    else:
        return False


N, L, R = map(int, input().split())
country_map = []
for i in range(N):
    row = list(map(int, input().split()))
    country_map.append(row)

result = 0
while True:
    is_move = False
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                if BFS(country_map, i, j):
                    is_move = True
    if not is_move:
        break
    result += 1

print(result)
