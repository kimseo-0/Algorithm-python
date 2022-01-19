import sys
input = sys.stdin.readline

# 1차 풀이
# position = input()
# # ord : string > 아스키코드
# x = (ord(position[0]) % ord('a')) + 1
# y = int(position[1])
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# count = 0
# for i in range(4):
#     for j in range(2):
#         nx = x + dx[i] + dx[i] + dy[j + 2]
#         ny = y + dy[i] + dy[i] + dy[j + 2]
#
#         if (1 <= nx) and (nx <= 8) and (1 <= ny) and (ny <= 8):
#             count += 1
#
# print(count)

# 2차 풀이
position = input()
# 입력의 제한이 있기 때문에 나머지가 아니라 빼기로 해도 충분하다
x = (ord(position[0]) - ord('a')) + 1
y = int(position[1])

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

count = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if (1 <= nx) and (nx <= 8) and (1 <= ny) and (ny <= 8):
        count += 1

print(count)
