import sys
from collections import deque

input = sys.stdin.readline

def BFS(graph, x, y):
    queue = deque([(x, y)])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # count = 1   # 현재 위치가 첫번째 칸으로부터 몇 칸 떨어져있는지 확인하는 변수
    # length = 0  # count 가 동일한 칸들의 수를 확인하는 변수
    while queue:
        # if length == 0:     # length 가 0이 되면
        #     count += 1      # count 가
        #     length = len(queue)
        # length -= 1
        v = queue.popleft()

        for node in range(4):
            nx = v[0] + dx[node]
            ny = v[1] + dy[node]
            if nx == 0 and ny == 0:
                continue
            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                # graph[nx][ny] = count
                graph[nx][ny] = graph[v[0]][v[1]] + 1   # 더 쉬운 방법! 이전 칸의 값 + 1
                queue.append((nx, ny))
                if nx == N - 1 and ny == M - 1:
                    return


N, M = map(int, input().split())
map_list = []
for i in range(N):
    map_list.append(list(map(int, list(input().strip()))))

BFS(map_list, 0, 0)


for i in range(N):
    print(map_list[i])


print(map_list[N - 1][M - 1])