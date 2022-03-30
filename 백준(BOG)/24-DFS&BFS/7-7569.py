import sys
from collections import deque

input = sys.stdin.readline

dCol = [0, 0, -1, 1, 0, 0]  # 위 아래 왼쪽 오른쪽 앞 뒤
dRow = [0, 0, 0, 0, 1, -1]
dHeight = [1, -1, 0, 0, 0, 0]

M, N, H = map(int, input().split())     # col, row, height
tomato_box = []
good_tomato_list = []
tomato_num = 0
for h in range(H):
    floor = []
    for i in range(N):
        row_list = list(map(int, input().split()))
        for j in range(M):
            if row_list[j] == 1:
                good_tomato_list.append((h, i, j))
                tomato_num += 1
            elif row_list[j] == 0:
                tomato_num += 1
        floor.append(row_list)
    tomato_box.append(floor)

def BFS(graph, starts, num):
    q = deque(starts)
    result = 0
    num -= len(starts)

    while q:
        (height, row, col) = q.popleft()

        for i in range(6):
            nHeight = height + dHeight[i]
            nRow = row + dRow[i]
            nCol = col + dCol[i]

            if nHeight <= -1 or nHeight >= H or nRow <= -1 or nRow >= N or nCol <= -1 or nCol >= M:
                continue
            if graph[nHeight][nRow][nCol] <= -1:
                continue
            if graph[nHeight][nRow][nCol] >= 1:
                continue

            graph[nHeight][nRow][nCol] = graph[height][row][col] + 1
            q.append((nHeight, nRow, nCol))
            result = max(result, graph[nHeight][nRow][nCol] - 1)
            num -= 1

    if num > 0:
        return -1
    else:
        return result


print(BFS(tomato_box, good_tomato_list, tomato_num))

# result = 0
# for floor in tomato_box:
#     for row in floor:
#         for tomato in row:
#             if tomato == 0:
#                 result = -1
#                 break
#             if tomato >= 1:
#                 result = max(result, tomato - 1)
#         if result == -1:
#             break
#     if result == -1:
#         break

# print(result)