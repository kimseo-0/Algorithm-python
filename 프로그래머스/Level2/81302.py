# 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302

dx1 = [-1, 0, 1, 0] # 위 아래 오른쪽 왼쪽
dy1 = [0, -1, 0, 1]

dx2 = [-1, 1, 1, -1]
dy2 = [-1, -1, 1, 1]

def check_place(place):
    for x in range(5):
        for y in range(5):
            if place[x][y] == 'P':
                for i in range(4):
                    for j in range(1, 3):
                        nx = x + dx1[i] * j
                        ny = y + dy1[i] * j

                        if nx <= -1 or nx >= 5 or ny <= -1 or ny >= 5:
                            break
                        if place[nx][ny] == 'X':
                            break
                        if place[nx][ny] == 'P':
                            return 0

                for i in range(4):
                    nx = x + dx2[i]
                    ny = y + dy2[i]

                    if nx <= -1 or nx >= 5 or ny <= -1 or ny >= 5:
                        continue
                    if place[nx][ny] == 'P':
                        if place[nx][y] != 'X' or place[x][ny] != 'X':
                            return 0
    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(check_place(place))

    return answer


# solution([["POOOO",
#            "OPXOX", "OOXOX", "OOXOX", "OOXXO"],
#           ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
#           ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
#           ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
#           ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
solution([["POOOO",
           "OPXOX", "OOXOX", "OOXOX", "OOXXO"]])
