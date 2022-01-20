import sys
input = sys.stdin.readline

# N * M map
N, M = map(int, input().split())
# 초기 위치 :(x, y), 초기 방향 : d
x, y, d = map(int, input().split())

# map 초기화
map_list = []
for i in range(N):
    map_list.append(list(map(int, input().split())))

# map에서
# 0 : 육지 & 방문 x
# 1 :바다
# 2 : 육지 & 방문 o

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = [0, 1, 2, 3]

# 현재 위치 방문 처리
map_list[x][y] = 2
count = 1
while True:
    # 갈 수 있는 새로운 칸이 있는지 확인
    is_movable = False

    # 네 방향 모두 갈 수 있는지 확인
    for i in range(4):
        # 왼쪽 방향으로 방향 회전
        d = direction[d - 1]
        nx = x + dx[d]
        ny = y + dy[d]

        # 갈 수 있는 방향이 확인 되면
        if map_list[nx][ny] == 0:
            print(nx, ny, d)

            # 갈 수 있으면 새로운 칸으로 이동
            x = nx
            y = ny
            count += 1

            # 갈 수 있으면 맵에 2로 표시
            map_list[nx][ny] = 2
            is_movable = True
            break

    # 모든 방향으로 갈 수 없음이 확인 되면
    if not is_movable:
        # 뒤로 한 칸
        nx = x + dx[direction[d - 2]]
        ny = y + dy[direction[d - 2]]

        # 뒤로 갈 수 있는지 확인, 바다이면 STOP
        if map_list[nx][ny] == 1:
            break
        else:
            # 갈 수 있으면 방향 이동
            print(nx, ny, d)
            x = nx
            y = ny

print(count)