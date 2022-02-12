from collections import deque


def BFS(graph, start_list):
    q = deque(start_list)

    while q:
        (z, x, y) = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
                continue
            if graph[nz][nx][ny] == -1 or graph[nz][nx][ny] == 1 or graph[nz][nx][ny] <= graph[z][x][y] + 1:
                continue
            if graph[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                graph[nz][nx][ny] = graph[z][x][y] + 1


M, N, H = map(int, input().split())
tomato_box = []
good_tomato_list = []
for i in range(H):
    floor = []
    for j in range(N):
        floor.append(list(map(int, input().split())))
        for k in range(M):
            if floor[j][k] == 1:
                good_tomato_list.append((i, j, k))
    tomato_box.append(floor)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

BFS(tomato_box, good_tomato_list)

isAvail = True
for floor in tomato_box:
    if not isAvail:
        break
    for row in floor:
        if row.count(0) != 0:
            isAvail = False
            print(-1)
            break
        print(row)

if isAvail:
    print(max(list(map(lambda x: max(list(map(max, x))), tomato_box))) - 1)
