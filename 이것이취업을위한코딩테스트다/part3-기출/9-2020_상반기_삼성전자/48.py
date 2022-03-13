N, M, k = map(int, input().split())

dx = [-1, 1, 0, 0]  # 위 아래 왼쪽 오른쪽
dy = [0, 0, -1, 1]

map_list = []
shark_position = [[0, 0, 0] for _ in range(M)]
shark_smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] != 0:
            shark_position[row[j] - 1] = [row[j], i, j]
            shark_smell[i][j] = [row[j], k]
    map_list.append(row)

shark_direction = list(map(lambda el: int(el) - 1, input().split()))

shark_priority = []
for i in range(M):
    row = []
    for j in range(4):
        row.append(list(map(lambda el: int(el) - 1, input().split())))
    shark_priority.append(row)

time = 0
while True:
    if M == 1:
        break
    if time >= 1000:
        time = -1
        break

    # for m in map_list:
    #     print(m)
    # for m in shark_smell:
    #     print(m)
    # print()

    for i in range(M):
        [current_num, x, y] = shark_position[i]
        current_direction = shark_direction[i]
        current_priority = shark_priority[i][current_direction]
        map_list[x][y] = 0

        change = False
        for di in current_priority:
            nx = x + dx[di]
            ny = y + dy[di]

            if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
                continue
            if shark_smell[nx][ny] != [0, 0]:
                continue
            change = True
            shark_position[i] = [current_num, nx, ny]
            shark_direction[i] = di
            break

        if change:
            continue

        for di in current_priority:
            nx = x + dx[di]
            ny = y + dy[di]

            if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
                continue
            if shark_smell[nx][ny][0] == current_num:
                shark_position[i] = [current_num, nx, ny]
                shark_direction[i] = di
                break

    for i in range(N):
        for j in range(N):
            if shark_smell[i][j] != [0, 0]:
                shark_smell[i][j][1] -= 1
                if shark_smell[i][j][1] == 0:
                    shark_smell[i][j] = [0, 0]

    for i in range(M):
        [current_num, x, y] = shark_position[i]
        if map_list[x][y] == 0:
            map_list[x][y] = current_num
            shark_smell[x][y] = [current_num, k]
        else:
            shark_position.pop(i)
            shark_direction.pop(i)
            shark_priority.pop(i)
            M -= 1

    time += 1
    # print(time)

print(time)
