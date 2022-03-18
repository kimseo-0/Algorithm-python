# 감시 피하기
# 바이러스 피하기 문제와 동일,
# 조합을 활용하여 장애물의 모든 조합에 대해서 체크한다.

from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def BFS(graph, starts):
    q = deque(starts)

    while q:
        (x, y) = q.popleft()

        for i in range(4):
            for n in range(1, N):
                nx = x + n * dx[i]
                ny = y + n * dy[i]

                # 영역 밖에 있는 경우
                if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
                    break
                # 선생님을 만난경우
                if graph[nx][ny] == 'T':
                    return False
                # 장애물을 만난경우
                if (nx, ny) in three_obstacle:
                    break
                # 학생을 만난경우
                if graph[nx][ny] == 'S':
                    break

    return True


N = int(input())
map_list = []
obstacle_avail_list = []
student_list = []

for i in range(N):
    row = list(input().split())
    for j in range(N):
        if row[j] == 'X':
            obstacle_avail_list.append((i, j))
        if row[j] == 'S':
            student_list.append((i, j))
    map_list.append(row)

# 설치 가능한 장애물 3개 조합
obstacle_avail_combination_list = list(combinations(obstacle_avail_list, 3))

result = False
for three_obstacle in obstacle_avail_combination_list:
    result = BFS(map_list, student_list)
    if result:
        break

if result:
    print('YES')
else:
    print('NO')
