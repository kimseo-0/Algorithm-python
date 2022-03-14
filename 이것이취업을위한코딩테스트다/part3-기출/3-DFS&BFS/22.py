import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]  # 아래, 위, 오른쪽, 왼쪽
dy = [0, 0, 1, -1]

def BFS(graph, visited, start, n, time):
    result = 10e9
    ((x1, y1), (x2, y2)) = start
    q = deque([start])
    visited[x1][y1] = time + 1
    visited[x2][y2] = time + 1

    print(start)
    for v in visited:
        print(v)
    print()

    while q:
        ((x1, y1), (x2, y2)) = q.popleft()

        for i in range(2):
            if y1 == y2:
                i = i + 2
            nx1 = x1 + dx[i]
            nx2 = x2 + dx[i]
            ny1 = y1 + dy[i]
            ny2 = y2 + dy[i]
            if nx1 <= -1 or nx1 >= n or nx2 <= -1 or nx2 >= n or ny1 <= -1 or ny1 >= n or ny2 <= -1 or ny2 >= n:
                continue
            if graph[nx1][ny1] == 1 or graph[nx2][ny2] == 1:
                continue

            # new_visited = deepcopy(visited)
            # new_visited[nx1][ny1] = new_visited[x1][y1]
            # new_visited[nx2][ny2] = new_visited[x1][y1]

            if visited[nx1][ny1] == 0:
                q.append(((nx1, ny1), (nx2, ny2)))
                # if x1 != nx1 and y1 != ny1:
                visited[nx1][ny1] = visited[x1][y1] + 1
                # if x2 != nx2 and y2 != ny2:
                visited[nx2][ny2] = visited[x1][y1] + 1

                if (nx1 == n - 1 and ny1 == n - 1) or (nx2 == n - 1 and ny2 == n - 1):
                    if visited[nx1][ny1] != 0:
                        result = min(result, visited[nx1][ny1])
                    break
            if visited[nx2][ny2] == 0:
                q.append(((nx1, ny1), (nx2, ny2)))
                # if x1 != nx1 and y1 != ny1:
                visited[nx1][ny1] = visited[x1][y1] + 1
                # if x2 != nx2 and y2 != ny2:
                visited[nx2][ny2] = visited[x1][y1] + 1

                if (nx1 == n - 1 and ny1 == n - 1) or (nx2 == n - 1 and ny2 == n - 1):
                    if visited[nx1][ny1] != 0:
                        result = min(result, visited[nx1][ny1])
                    break

        for i in range(4):
            nx1 = x1 + dx[i]
            nx2 = x2 + dx[i]
            ny1 = y1 + dy[i]
            ny2 = y2 + dy[i]

            if nx1 <= -1 or nx1 >= n or nx2 <= -1 or nx2 >= n or ny1 <= -1 or ny1 >= n or ny2 <= -1 or ny2 >= n:
                continue
            if graph[nx1][ny1] == 1 or graph[nx2][ny2] == 1:
                continue
            if visited[nx1][ny1] > 0 and visited[nx2][ny2] > 0:
                continue

            q.append(((nx1, ny1), (nx2, ny2)))
            # if x1 != nx1 and y1 != ny1:
            visited[nx1][ny1] = visited[x1][y1] + 1
            # if x2 != nx2 and y2 != ny2:
            visited[nx2][ny2] = visited[x1][y1] + 1

            if (nx1 == n - 1 and ny1 == n - 1) or (nx2 == n - 1 and ny2 == n - 1):
                if visited[nx1][ny1] != 0:
                    result = min(result, visited[nx1][ny1])
                break

    return result

def solution(board):
    n = len(board)
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    visited[0][1] = 1
    answer = BFS(board, visited, ((0, 0), (0, 1)), n, 0)
    # print(answer - 1)
    return answer - 1


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
