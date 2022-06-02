# 피로도
# https://programmers.co.kr/learn/courses/30/lessons/87946
import itertools


def solution(k, dungeons):
    answer = 0

    dungeons_list = list(itertools.permutations(dungeons))

    for dungeons in dungeons_list:
        count = 0
        hp = k
        for dungeon in dungeons:
            if hp >= dungeon[0]:
                hp -= dungeon[1]
                count += 1

        if answer < count:
            answer = count

    return answer

