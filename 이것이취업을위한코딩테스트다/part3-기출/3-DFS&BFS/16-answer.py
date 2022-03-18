from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 입력 값
N, M = map(int, input().split())

data = []   # 초기 맵
temp = [[0] * M for _ in range(N)]  # 벽 설치 맵

result = 0

# 바이러스가 사방으로 퍼짐
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if temp[nx][ny] != 0:
            continue

        temp[nx][ny] = 2
        virus(nx, ny)

# 현재 맵 상태에서 안전 영역 크기 계산
def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    return score

def DFS(count):
    global result

    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = data[i][j]

        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return

    # 울타리가 3개 미만인 경우 울타리 설치
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                DFS(count)
                data[i][j] = 0
                count -= 1


DFS(0)
print(result)