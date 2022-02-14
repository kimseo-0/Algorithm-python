# 시작 08:15 - 종료 09:05

# N * M 직사각형
# 바이러스 상하좌우 퍼짐
# 벽은 반드시 3개 세워야함
# 0 : 빈칸, 1 : 벽, 2 : 바이러스
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline


def BFS(graph, start_list, result):
    q = deque(start_list)

    while q:
        (x, y) = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 영역 밖
            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue
            # 기존 벽 or 새로 세운 벽
            if graph[nx][ny] == 1 or visited_list[nx][ny] == 1:
                continue
            # 초기 바이러스와 추가된 바이러스
            if visited_list[nx][ny] == 2 or graph[nx][ny] == 2:
                continue
            # 추가 바이스러 전염 가능 영역
            if graph[nx][ny] == 0:
                q.append((nx, ny))
                visited_list[nx][ny] = 2
                # 안전 영역 -1
                result -= 1
    return result


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 입력 값
N, M = map(int, input().split())

map_list = []   # 전체 맵
start_virus_list = []       # 초기 바이러스 위치 리스트
available_wall_list = []    # 추가 벽 가능 영역 리스트, 즉 벽과 바이러스가 없는 위치 리스트

current_safe_zone = 0       # 현재 안전 영역
max_safe_zone = 0           # 최대 안전 영역

# 입력 값
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 2:
            # 바이러스
            start_virus_list.append((i, j))
        elif row[j] == 0:
            # 빈칸 : 새로운 벽 추가 가능 영역
            available_wall_list.append((i, j))
    map_list.append(row)

# 가능한 추가 벽 중 3개를 고르는 모든 경우의 수(조합)
available_wall_combination_list = list(combinations(available_wall_list, 3))

# 모든 빈칸(초기 안전 영역) - 3
# 가능한 벽의 수를 3개 추가했으므로 안전영역 -3
current_safe_zone = len(available_wall_list) - 3

for available_wall_combination in available_wall_combination_list:
    # 새로 퍼진 바이러스를 저장
    visited_list = [[0] * M for _ in range(N)]
    for available_wall in available_wall_combination:
        visited_list[available_wall[0]][available_wall[1]] = 1

    # 기존 최대 안전 영역 vs 새로운 안전 영역
    max_safe_zone = max(max_safe_zone, BFS(map_list, start_virus_list, current_safe_zone))

print(max_safe_zone)

# 이번 문제 풀 때 생각의 흐름
# 1. 벽을 세우는 규칙이 있을까? > 일부 경우 조건?
# 2. 규칙이 없다, 모든 가능한 경우를 다 돌아야 할까? > 모든 경우?
# 3. 입력값의 범위를 보고, 최대 경우를 계산해보니 시간 제한 내에서 가능할 것 같다. > 입력값 범위 확인

# 이때 1번에 매몰되어 2, 3으로 넘어가지 못한다면 시간 안에 문제를 풀 수 없다.
# 생각의 흐름을 약간 바꾼다면 더 빠르게 풀 수 있을 것이다.

# 1번을 생각하기 전, 입력값의 범위를 먼저 확인한다.

# step 0. 입력값의 범위를 확인하고, 모든 경우의 수를 돌아도 시간 제한 내에서 가능할까?
# step 1. 모든 경우의 수를 돌지 않도록, 조건을 통해 일부의 경우만 돌게 할 수 있을까?

# step 2. step 0에서 yes, step 1에서 no > 모든 경우 확인
# step 2. step 0에서 yes, step 1에서 yes > 모든 경우 확인 or 조건을 통해 일부 경우만 확인

# step 3. step 0에서 no인 경우
# > 반드시 조건을 통해 일부 경우만 확인
# > 특정 알고리즘들의 Big O를 체크 하여 시간 제한을 고려해야하는 문제

# 입력값의 범위는 출제자의 힌트다.
