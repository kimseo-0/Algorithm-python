import sys
input = sys.stdin.readline

# 초기화
N = int(input())
map_list = [[0] * (N + 1) for _ in range(N + 1)]

K = int(input())
for i in range(K):
    a, b = map(int, input().split())
    map_list[a][b] = 1

L = int(input())
direction_list = []
for i in range(L):
    t, direction = input().split()
    direction_list.append((int(t), direction))

# 순서대로 오른쪽 방향으로 90도 돌렸을 때 나오는 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 지도상 표시들, 원하는 숫자로 표기하자
apple_num = 1
snake_num = 2

# 뱀 상태 초기화
snake_size = 1
snake_head = (1, 1)         # 뱀 머리 위치
snake_position = [(1, 1)]   # 뱀이 위치한 모든 좌표
map_list[1][1] = snake_num  # 지도에 뱀 위치 표시
snake_direction = 0         # 뱀 이동 방향 : 오른쪽

time = 0
while True:
    time += 1

    # 뱀의 머리 정보
    (x, y) = snake_head
    nx = x + dx[snake_direction]
    ny = y + dy[snake_direction]

    # 이동할 수 없는 영역
    if nx <= 0 or nx >= N + 1 or ny <= 0 or ny >= N + 1:
        break
    # 뱀이 자신의 몸을 만난 경우
    if map_list[nx][ny] == snake_num:
        break

    # 뱀이 사과를 만난 경우 : 뱀 사이즈 증가 및 뱀 위치 증가
    if map_list[nx][ny] == apple_num:
        snake_size += 1
        snake_head = (nx, ny)
        snake_position.append((nx, ny))
        map_list[nx][ny] = snake_num

    # 뱀이 빈칸을 만난 경우 : 뱀 사이즈 유지, 뱀 머리 위치 추가, 뱀 꼬리 위치 삭제
    else:
        snake_head = (nx, ny)
        snake_position.append((nx, ny))
        map_list[nx][ny] = snake_num

        # 뱀 꼬리 위치 삭제
        (x, y) = snake_position.pop(0)
        map_list[x][y] = 0

    # 이동 방향 체크
    # 이동 방향을 바꿔야 하는 경우
    if len(direction_list) != 0 and time == direction_list[0][0]:
        # 오른쪽 90도 회전
        if direction_list[0][1] == 'D':
            snake_direction = (snake_direction + 1) % 4
        # 왼쪽 90도 회전
        else:
            snake_direction = (snake_direction - 1) % 4

        # 확인한 (시간, 방향) 정보 삭제
        direction_list.pop(0)

print(time)
