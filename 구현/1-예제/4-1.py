import sys
input = sys.stdin.readline

# 1차 풀이

# N = int(input())
# plan = list(input().split())
# N = 5
# plan = ["R", "R", "R", "U", "D", "D"]

# x = 1
# y = 1
# for i in plan:
#     if i == "L":
#         x = 1 if (x == 1) else x - 1
#     elif i == "R":
#         x = N if (x == N) else x + 1
#     elif i == "U":
#         y = 1 if (y == 1) else y - 1
#     elif i == "D":
#         y = N if (y == N) else y + 1
#
#     # if x < 1:
#     #     x = 1
#     # elif x > N:
#     #     x = N
#     # if y < 1:
#     #     y = 1
#     # elif y > N:
#     #     y = N
#
# print(x, y)

# 2차 풀이
# 위치 문제의 경우 dx, dy를 활용한 표현법을 사용하면 좋다
# N = int(input())
# plan = list(input().split())
N = 5
plan = ["R", "R", "R", "U", "D", "D"]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction_type = ["L", "R", "U", "D"]

x = 1
y = 1
for direction in plan:
    nx = x + dx[direction_type.index(direction)]
    ny = y + dy[direction_type.index(direction)]

    if (1 <= nx) and (nx <= N) and (1 <= ny) and (ny <= N) :
        x = nx
        y = ny

print(x, y)     # 4 3
