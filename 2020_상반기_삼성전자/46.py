# 아기상어의 크기 2, 모든 물고기는 크기가 있음(자연수)
# 아기상어는 상하좌우 인접한 한칸씩 이동
# 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다
from collections import deque
import sys
input = sys.stdin.readline


def BFS(graph, start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    result_list = []

    while queue:
        (x, y) = queue.popleft()

        # 결과값을 더이상 받을 필요 없는 상황 :
        # 먹을 수 있는 물고기가 더 있더라도 더 짧은 거리에 먹을 물고기가 있으므로 확인할 필요 없음
        if len(result_list) >= 1 and visited[x][y] + 1 > result_list[0][0]:
            return result_list

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 갈 수 없는 영역 : 맵 밖
            if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
                continue
            # 이미 방문한 영역 영역
            if visited[nx][ny] != 0:
                continue
            # 갈 수 없는 영역 : 자신보다 큰 물고기
            if graph[nx][ny] > size:
                continue
            # 갈 수 있는 영역 : 물고기가 없거나 동일한 크기의 물고기
            if graph[nx][ny] == 0 or graph[nx][ny] == size:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1             # 해당 영역까지의 거리(= 시간)
                continue
            # 갈 수 있고 먹을 수 있는 영역 : 자신보다 작은 물고기
            if graph[nx][ny] < size:
                visited[nx][ny] = visited[x][y] + 1
                result_list.append((visited[nx][ny], nx, ny))   # (해당 영역까지 거리, x, y)

            # 결과값을 더이상 받을 필요 없는 상황 :
            # 먹을 수 있는 물고기가 더 있더라도 더 짧은 거리에 먹을 물고기가 있으므로 확인할 필요 없음
            # if len(result_list) >= 1 and visited[nx][ny] > visited[result_list[0][1]][result_list[0][2]]:
            #     return result_list

    return result_list


N = int(input())

current = (0, 0)    # 현재 위치
time = 0    # 총 걸리는 시간
size = 2    # 현재 사이즈
count = 0   # 사이즈 업 전, 지금까지 먹은 물고기 수

map_list = []   # 그래프
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 9:
            current = (i, j)
            row[j] = 0
    map_list.append(row)

dx = [-1, 0, 0, 1]  # 위 왼쪽 오른쪽 아래
dy = [0, -1, 1, 0]

while True:
    visited = [[0] * N for _ in range(N)]   # 방문 처리용 이중 리스트
    result = BFS(map_list, current)

    # 결과값이 더이상 없는 경우 종료 : 더이상 먹을 물고기가 없는 상황
    if len(result) == 0:
        break

    result.sort()   # (거리, x, y) 순으로 정렬
    (cost, row, col) = result[0]    # 거리가 가장 짧은 것 중에서 가장 위(x) 가장 왼쪽(y)
    current = (row, col)            # 현재 위치 수정
    map_list[row][col] = 0          # 맵 갱신 : 먹은 물고기 위치 0
    count += 1                  # 먹은 물고기 수 갱신 : +1
    time += cost                # 총 걸린 시간 갱신

    # size 만큼 물고기를 먹은 경우
    # 먹은 물고기수, 현재 사이즈 갱신
    if count == size:
        count = 0
        size += 1

print(time)
