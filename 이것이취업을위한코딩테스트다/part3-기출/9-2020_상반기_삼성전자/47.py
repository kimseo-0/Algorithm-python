# 청소년 상어
import sys
from copy import deepcopy

input = sys.stdin.readline


dx = [-1, -1, 0, 1, 1, 1, 0, -1]   # 위 부터 시계 반대 방향
dy = [0, -1, -1, -1, 0, 1, 1, 1]

N = 4

def move_fishes(map_list, fishes):
    for fish in fishes:
        if fish == -1:
            continue

        [num, direction, x, y] = fish
        for i in range(8):
            new_direction = (direction + i) % 8
            nx = x + dx[new_direction]
            ny = y + dy[new_direction]

            if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
                continue

            temp_num = map_list[nx][ny]
            if temp_num == 17:
                continue
            if temp_num != -1:
                fishes[temp_num][2] = x
                fishes[temp_num][3] = y

            fishes[num][1] = new_direction
            fishes[num][2] = nx
            fishes[num][3] = ny
            map_list[nx][ny] = num
            map_list[x][y] = temp_num

            break

def find_avail_fish(map_list, shark):
    result = []
    # 먹을 수 있는 물고기
    for i in range(1, 4):
        [num, direction, x, y] = shark
        nx = x + i * dx[direction]
        ny = y + i * dy[direction]

        if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
            break
        if map_list[nx][ny] == -1:
            continue
        result.append(map_list[nx][ny])

    return result

def DFS(map_list, fishes, shark, shark_size):
    result = []

    # 물고기 이동
    move_fishes(map_list, fishes)
    # 상어가 이동 가능한 물고기 번호
    avail_fishes_num = find_avail_fish(map_list, shark)

    # 더이상 상어가 이동 불가능 할 경우 종료
    if len(avail_fishes_num) == 0:
        return shark_size

    for fish_num in avail_fishes_num:
        # 상어가 먹은 물고기에 따라
        # 지도, 물고기 상태, 상어 상태, 총 먹은 물고기가 달라지므로 copy 가 필요하다.
        new_map_list = deepcopy(map_list)
        new_fishes = deepcopy(fishes)
        new_shark = deepcopy(shark)
        new_shark_size = shark_size

        # 상어 물고기 먹기 단계
        [_, _, x, y] = new_shark                  # 상어 현재 상태
        [num, _, nx, ny] = new_fishes[fish_num]   # 먹을 물고기 현재 상태
        new_map_list[x][y] = -1                   # 상어 이동, 지도 빈칸 표기
        new_shark = new_fishes[num]               # 이동한 상어 상태 초기화
        new_shark[0] = 17                         # 상어 번호 초기화
        new_fishes[num] = -1                      # 먹은 물고기 상태 초기화
        new_shark_size += (fish_num + 1)          # 상어가 먹은 물고기 추가
        new_map_list[nx][ny] = 17                 # 지도 상어 표기

        # 상어 물고기 먹기 단계
        new_shark_size = DFS(new_map_list, new_fishes, new_shark, new_shark_size)
        result.append(new_shark_size)

    # 결과 값들 중 가장 큰 값을 return
    return max(result)


# 초기화
base_map_list = []
base_fishes = []     # 0 ~ 15번 물고기

for i in range(N):
    # 전체적으로 index 를 맞추기 위해서
    # 물고기 번호와 물고기 방향을 -1 해서 처리함
    num1, dir1, num2, dir2, num3, dir3, num4, dir4 = map(lambda el: int(el) - 1, input().split())
    row = [(num1, dir1), (num2, dir2), (num3, dir3), (num4, dir4)]
    base_map_list.append([num1, num2, num3, num4])
    base_fishes.extend([[num1, dir1, i, 0], [num2, dir2, i, 1], [num3, dir3, i, 2], [num4, dir4, i, 3]])
base_fishes.sort()

# 상어 초기화
base_shark_size = 0   # 상어가 먹은 물고기 양
base_shark = base_fishes[base_map_list[0][0]]  # 상어 상태
base_shark[0] = 17  # 상어 번호 초기화
base_fishes[base_map_list[0][0]] = -1     # 물고기 먹음
base_shark_size += (base_map_list[0][0] + 1)  # 상어가 먹을 물고기 추가
base_map_list[0][0] = 17    # 지도 상어 표기

print(DFS(base_map_list, base_fishes, base_shark, base_shark_size))

