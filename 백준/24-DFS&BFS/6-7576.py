import sys
from collections import deque

input = sys.stdin.readline

def print_box(graph):
    for row in graph:
        print(row)

def BFS(graph, x, y, start_list):
    # queue = deque([(x, y)])
    queue = deque(start_list)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    # length = 0
    # count = 1
    while queue:
        # print(queue)
        # if length == 0:
        #     length = len(queue)
        #     count += 1
        (x, y) = queue.popleft()
        # length -= 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx <= -1 or nx >= M or ny <= -1 or ny >= N or graph[nx][ny] == -1 or graph[nx][ny] >= 1: #== 1:
                continue
            # if (1 <= graph[nx][ny]) and (graph[nx][ny] <= count):
            #     continue
            if graph[nx][ny] == 0:  # or graph[nx][ny] > count:
                # graph[nx][ny] = count
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

def DFS(graph, x, y, count):
    if x <= -1 or x >= M or y <= -1 or y >= N or graph[x][y] == -1:
        return
    if count != 1 and (1 <= graph[x][y]) and (graph[x][y] <= count):
        return
    print(x, y, count)
    print_box(graph)

    graph[x][y] = count

    DFS(graph, x + 1, y, count + 1)
    DFS(graph, x - 1, y, count + 1)
    DFS(graph, x, y + 1, count + 1)
    DFS(graph, x, y - 1, count + 1)
    return True


N, M = map(int, input().split())
tomato_box = []
good_tomato_list = []
for i in range(M):
    tomato_box_row = list(map(int, input().split()))
    for j in range(N):
        if tomato_box_row[j] == 1:
            good_tomato_list.append((i, j))
    tomato_box.append(tomato_box_row)

# for num in range(count_good_tomato):
#     for i in range(M):
#         for j in range(N):
#             if tomato_box[i][j] == 1:
#                 BFS(tomato_box, i, j, good_tomato_list)
#                 # DFS(tomato_box, i, j, 1)
#                 # print(tomato_box)

BFS(tomato_box, i, j, good_tomato_list)

isAvail = 1
for i in range(M):
    if tomato_box[i].count(0) != 0:
        isAvail = 0
        print(-1)
        break

if isAvail:
    print(max(list(map(max, tomato_box))) - 1)

