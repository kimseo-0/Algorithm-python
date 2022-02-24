import heapq
INF = 10e9

def dijkstra(start):
    q = []
    (cost, (x, y)) = start
    heapq.heappush(q, (cost, (x, y)))
    distance[x][y] = cost

    while q:
        dist, (x, y) = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for new_cost, (nx, ny) in graph[x][y]:
            cost = dist + new_cost
            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, (nx, ny)))


# 위 아래 왼 오
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())    # 테스트 케이스 수
result = []
for t in range(T):
    N = int(input())
    graph = [[[] for _ in range(N)] for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]
    start = None
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
                    continue
                else:
                    graph[nx][ny].append((row[j], (i, j)))

                if i == 0 and j == 0:
                    start = (row[j], (i, j))

            # if i == 0 and j == 0:
            #     start = (row[j], (i, j))
            #     graph[i][j + 1].append((row[j], (i, j)))
            #     graph[i + 1][j].append((row[j], (i, j)))
            # elif i == N - 1 and j == N - 1:
            #     graph[i - 1][j].append((row[j], (i, j)))
            #     graph[i][j - 1].append((row[j], (i, j)))
            # elif i == 0 and j == N - 1:
            #     graph[i + 1][j].append((row[j], (i, j)))
            #     graph[i][j - 1].append((row[j], (i, j)))
            # elif i == N - 1 and j == 0:
            #     graph[i - 1][j].append((row[j], (i, j)))
            #     graph[i][j + 1].append((row[j], (i, j)))
            # elif i == 0:
            #     graph[i][j + 1].append((row[j], (i, j)))
            #     graph[i][j - 1].append((row[j], (i, j)))
            #     graph[i + 1][j + 1].append((row[j], (i, j)))
            # elif j == 0:
            #     graph[i - 1][j].append((row[j], (i, j)))
            #     graph[i + 1][j].append((row[j], (i, j)))
            #     graph[i][j + 1].append((row[j], (i, j)))
            # elif i == N - 1:
            #     graph[i - 1][j].append((row[j], (i, j)))
            #     graph[i][j - 1].append((row[j], (i, j)))
            #     graph[i][j + 1].append((row[j], (i, j)))
            # elif j == N - 1:
            #     graph[i][j - 1].append((row[j], (i, j)))
            #     graph[i - 1][j].append((row[j], (i, j)))
            #     graph[i + 1][j].append((row[j], (i, j)))
            # else:
            #     graph[i][j + 1].append((row[j], (i, j + 1)))
            #     graph[i][j - 1].append((row[j], (i, j - 1)))
            #     graph[i - 1][j].append((row[j], (i - 1, j)))
            #     graph[i + 1][j].append((row[j], (i + 1, j)))

    dijkstra(start)
    print(graph)
    print(distance)
    result.append(distance[N - 1][N - 1])

for i in result:
    print(i)
