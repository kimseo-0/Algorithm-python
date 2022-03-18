# 경쟁적 전염

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# num : 바이러스 번호
def BFS(graph, start_list, num):
    q = deque(start_list)
    virus_list[num] = []

    while q:
        (x, y) = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 영역 밖
            if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
                continue
            # 이미 바이러스가 잇는 곳
            if graph[nx][ny] > 0:
                continue
            # 바이스러 전염 가능 영역
            if graph[nx][ny] == 0:
                virus_list[num].append((nx, ny))
                graph[nx][ny] = num


N, K = map(int, input().split())
map_list = [[0] * N for _ in range(N)]
# [[], [[x, y]], [], []]
virus_list = [[] for _ in range(K + 1)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] > 0:
            map_list[i][j] = row[j]
            virus_list[row[j]].append((i, j))

S, X, Y = map(int, input().split())

# 시간 만큼 반복
for time in range(S):
    # 바이러스 종류 만큼 반복
    for i in range(1, K + 1):
        BFS(map_list, virus_list[i], i)

print(map_list[X - 1][Y - 1])
