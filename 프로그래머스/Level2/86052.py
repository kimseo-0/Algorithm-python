# 빛의 경로 사이클

dx = [-1, 0, 1, 0]  # 위 왼 아 오
dy = [0, -1, 0, 1]

def solution(grid):
    answer = []

    row = len(grid)
    col = len(grid[0])

    edges = [[[1 for _ in range(4)] for _ in range(col)] for _ in range(row)]

    while True:
        x, y, d = -1, -1, -1
        flag = False
        for i in range(row):
            for j in range(col):
                for k in range(4):
                    if edges[i][j][k] == 1:
                        flag = True
                        x, y, d = i, j, k
                        break
                if flag:
                    break
            if flag:
                break

        if not flag:
            break

        count = 0
        nx, ny, nd = x, y, d
        while True:
            # print(count, nx, ny, nd)
            nx = (nx + dx[nd]) % row
            ny = (ny + dy[nd]) % col
            count += 1

            if grid[nx][ny] == 'L':
                nd = (nd + 1) % 4
            if grid[nx][ny] == 'R':
                nd = (nd - 1) % 4

            edges[nx][ny][nd] = 0

            if nx == x and ny == y and nd == d:
                answer.append(count)
                break

    answer.sort()
    # print(answer)
    return answer

solution(["SL", "LR"])
