# 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062
import itertools


def solution(n, weak, dist):
    answer = len(dist) + 1
    num = len(weak)

    for i in range(num):
        weak.append(weak[i] + n)

    dist_list = list(itertools.permutations(dist))

    for start in range(num):
        for dist in dist_list:
            count = 1
            position = weak[start] + dist[count - 1]
            for i in range(start, start + num):
                # print(i, weak)
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i] + dist[count - 1]
            answer = min(answer, count)

            # print(answer)

    if answer > len(dist):
        return -1
    return answer


solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
# solution(12, [1, 3, 4, 9, 10], [3, 5, 7])
