from collections import deque

INF = 10e9

dx = [-1, 0, 1, 0]  # 위 왼 아 오
dy = [0, -1, 0, 1]

def BFS(graph, costs, N):
    queue = deque([(0, 0, -1)])
    costs[0][0] = 0

    while queue:
        (x, y, d) = queue.popleft()

        for i in range(4):
            if (d + 2) % 4 == i:
                continue

            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                continue

            new_cost = 0
            if d == i or d == -1:
                new_cost = costs[x][y] + 100
            else:
                new_cost = costs[x][y] + 600

            queue.append((nx, ny, i))
            costs[nx][ny] = new_cost


def solution(board):
    answer = 0
    n = len(board)
    costs = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        if board[0][i] == 1:
            break
        costs[0][i][1] = i * 100

    for i in range(n):
        if board[i][0] == 1:
            break
        costs[i][0][0] = i * 100

    for i in range(1, n):
        for j in range(1, n):
            if board[0][i] == 1:
                continue

            print(i, j)
            for d in range(4):
                new_cost = []
                x = i
                y = j
                if d == 0:
                    x -= 1
                elif d == 1:
                    y -= 1
                elif d == 2:
                    x += 1
                elif d == 3:
                    y += 1

                if x >= n or y >= n:
                    continue

                for n in range(4):
                    if d == n:
                        new_cost.append(costs[x][y][n] + 100)
                    elif (d + 2) % 4 == n:
                        new_cost.append(INF)
                    else:
                        new_cost.append(costs[x][y][n] + 600)

                costs[i][j][d] = min(new_cost)
                # print(i, j, d, new_cost)

    for i in costs:
        for j in i:
            for k in j:
                if k == INF:
                    print("INF", end=" ")
                else:
                    print(str(k), end=" ")
            print(",", end=" ")
        print()

    return answer


# solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]])
