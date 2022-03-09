import sys
input = sys.stdin.readline


def check_add_pillar(building_floor, building_pillar, x, y, n):
    if y == 0:
        return True
    if y == n:
        return False
    if x == 0:
        if building_floor[x][y] or building_pillar[x][y - 1]:
            return True
        return False
    if x == n:
        if building_floor[x - 1][y] or building_pillar[x][y - 1]:
            return True
        return False

    if building_floor[x][y] or building_floor[x - 1][y] or building_pillar[x][y - 1]:
        return True

    return False

def check_add_floor(building_floor, building_pillar, x, y, n):
    if y == 0:
        return False
    if x == n:
        return False
    if x == 0:
        if building_pillar[x][y - 1] or building_pillar[x + 1][y - 1]:
            return True
        if building_floor[x + 1][y]:
            return True
        return False
    if x == n - 1:
        if building_floor[x - 1][y]:
            return True
        if building_pillar[x][y - 1] or building_pillar[x + 1][y - 1]:
            return True

    if building_floor[x - 1][y] and building_floor[x + 1][y]:
        return True
    if building_pillar[x][y - 1] or building_pillar[x + 1][y - 1]:
        return True

    return False

def check_delete_pillar(answer, building_floor, building_pillar, x, y, n):
    check = True
    building_pillar[x][y] = False
    for frame in answer:
        [nx, ny, type] = frame
        if nx == x and ny == y:
            continue

        if type == 0:
            building_pillar[nx][ny] = False
            check = check_add_pillar(building_floor, building_pillar, nx, ny, n)
            building_pillar[nx][ny] = True
        else:
            building_floor[nx][ny] = False
            check = check_add_floor(building_floor, building_pillar, nx, ny, n)
            building_floor[nx][ny] = True

        if not check:
            break

    building_pillar[x][y] = True
    return check

def check_delete_floor(answer, building_floor, building_pillar, x, y, n):
    check = True
    building_floor[x][y] = False
    for frame in answer:
        [nx, ny, type] = frame
        if nx == x and ny == y:
            continue

        if type == 0:
            building_pillar[nx][ny] = False
            check = check_add_pillar(building_floor, building_pillar, nx, ny, n)
            building_pillar[nx][ny] = True
        else:
            building_floor[nx][ny] = False
            check = check_add_floor(building_floor, building_pillar, nx, ny, n)
            building_floor[nx][ny] = True

        if not check:
            break

    building_floor[x][y] = True
    return check

def solution(n, build_frame):
    answer = []
    building_floor = [[False] * (n + 1) for _ in range(n + 1)]
    building_pillar = [[False] * (n + 1) for _ in range(n + 1)]
    check = True
    for frame in build_frame:
        [x, y, type, action] = frame
        if action == 1:  # 추가
            if type == 0:   # 기둥
                check = check_add_pillar(building_floor, building_pillar, x, y, n)
            else:   # 보
                check = check_add_floor(building_floor, building_pillar, x, y, n)
        else:   # 삭제
            if type == 0:
                check = check_delete_pillar(answer, building_floor, building_pillar, x, y, n)
            else:
                check = check_delete_floor(answer, building_floor, building_pillar, x, y, n)

        if check:
            if action == 1:
                answer.append([x, y, type])
                if type == 0:
                    building_pillar[x][y] = True
                else:
                    building_floor[x][y] = True
            else:
                answer.remove([x, y, type])
                if action == 0:
                    if type == 0:
                        building_pillar[x][y] = False
                    else:
                        building_floor[x][y] = False

    answer.sort()
    print(answer)
    return answer


solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
