# DFS 활용

import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]   # 위 부터 시계 반대 방향
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def fish_move(shark_current, map_list, fish):
    # 물고기 이동
    for i in range(1, len(fish)):
        num, direction, x, y = fish[i]
        if num == 0:
            continue
        for n in range(0, 8):
            new_direction = (direction - 1 + n) % 8
            nx = x + dx[new_direction]  # 현재 방향부터 8번 회전
            ny = y + dy[new_direction]  # 현재 방향부터 8번 회전

            if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
                continue
            if shark_current == (nx, ny):
                continue

            temp = map_list[nx][ny]
            map_list[nx][ny] = (num, new_direction + 1)
            map_list[x][y] = temp

            fish[i] = (num, new_direction + 1, nx, ny)
            fish[map_list[x][y][0]] = (map_list[x][y][0], map_list[x][y][1], x, y)

            break
    return map_list

def find_avail_fish(shark_current, shark, map_list, fish):
    is_avail_fish = []
    # 먹을 수 있는 물고기
    for i in range(1, 4):
        x, y = shark_current
        new_direction = shark[1] - 1
        nx = x + i * dx[new_direction]
        ny = y + i * dy[new_direction]

        if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
            break
        if map_list[nx][ny] == (0, 0):
            continue
        is_avail_fish.append(fish[map_list[nx][ny][0]])
    return is_avail_fish

def shark_move(shark_current, shark, shark_eat, map_list, fish, is_avail_fish):
    result = []
    print(shark, shark_current, shark_eat)
    print(is_avail_fish)
    new_shark_eat = shark_eat
    new_map_list = copy.deepcopy(map_list)
    new_fish = copy.deepcopy(fish)
    while len(is_avail_fish) != 0:
        # 상어 이동
        new_shark_eat = shark_eat
        for i in range(len(is_avail_fish)):
            print(i)
            num, direction, x, y = is_avail_fish[i]
            new_shark_current = (x, y)
            new_shark = (num, direction)
            new_shark_eat += new_shark[0]
            new_map_list[shark_current[0]][shark_current[1]] = (0, 0)
            new_map_list[x][y] = (-1, -1)
            new_fish[num] = (0, 0, 0, 0)

            new_map_list = fish_move(new_shark_current, new_map_list, new_fish)
            for m in map_list:
                print(m)
            print()
            new_is_avail_fish = find_avail_fish(new_shark_current, new_shark, new_map_list, new_fish)
            new_shark_eat = shark_move(new_shark_current, new_shark, new_shark_eat,
                                       new_map_list, new_fish, new_is_avail_fish)
            new_shark_eat = shark_eat
            new_map_list = copy.deepcopy(map_list)
            new_fish = copy.deepcopy(fish)

    result.append(new_shark_eat)
    print('end')
    print()
    return new_shark_eat


# 초기화
N = 4
map_list = []
fish = [(0, 0)]

for i in range(N):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    row = [(a1, b1), (a2, b2), (a3, b3), (a4, b4)]
    map_list.append([(a1, b1), (a2, b2), (a3, b3), (a4, b4)])
    fish.extend([(a1, b1, i, 0), (a2, b2, i, 1), (a3, b3, i, 2), (a4, b4, i, 3)])
fish.sort()

# 상어 초기화
shark_eat = 0
visited = [[0] * N for _ in range(N)]

# (0,0) 물고기 먹음
shark_current = (0, 0)
shark = map_list[0][0]
shark_eat += shark[0]
map_list[0][0] = (-1, -1)
fish[shark[0]] = (0, 0, 0, 0)

fish_move(shark_current, map_list, fish)
is_avail_fish = find_avail_fish(shark_current, shark, map_list, fish)
shark_eat = shark_move(shark_current, shark, shark_eat, map_list, fish, is_avail_fish)

print(shark_eat)
