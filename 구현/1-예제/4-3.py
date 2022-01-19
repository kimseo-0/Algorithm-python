import sys

input = sys.stdin.readline

position = input()
x = (ord(position[0]) % ord('a')) + 1
y = int(position[1])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
for i in range(4):
    for j in range(2):
        nx = x + dx[i] + dx[i] + dy[j + 2]
        ny = y + dy[i] + dy[i] + dy[j + 2]

        if (1 <= nx) and (nx <= 8) and (1 <= ny) and (ny <= 8):
            print(i, j + 2)
            count += 1

print(count)
