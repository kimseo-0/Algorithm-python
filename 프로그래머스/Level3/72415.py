# 카드 짝 맞추기
# https://programmers.co.kr/learn/courses/30/lessons/72415
from copy import deepcopy

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

def min_count(board, x, y, nx, ny):


def DFS(board, x, y, count):
    for i in range(4):
        for j in range(1, 4):
            new_board = deepcopy(board)

            nx = x + j * dx[i]
            ny = y + j * dy[i]

            if nx <= -1 or nx >= 4 or ny <= -1 or ny >= 4:
                break

            if new_board[nx][ny] == 0:
                continue

            new_board[nx][ny] = 0
            if j == 3:
                DFS(new_board, nx, ny, count + 2)
            else:
                DFS(new_board, nx, ny, count + j)


def solution(board, r, c):
    answer = 0



    return answer
