import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []

for i in range(N):
    board.append(list(input()))

color_type = ["W", "B"]
min_count = N * M
# 전체 체스판에서 가능한 모든 8x8 사이즈
for row in range(N - 7):
    for col in range(M - 7):
        # 첫번째 체스칸이 "W"일 때와 "B"일때 고려
        for i in range(2):
            count = 0
            for j in range(8):
                for k in range(8):
                    if color_type[(i + j + k) % 2] != board[row + j][col + k]:
                        count += 1

            if min_count > count:
                min_count = count

print(min_count)