# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586
import math

def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:

        progress = progresses.pop(0)
        speed = speeds.pop(0)
        count = 1

        days = math.ceil(((100 - progress) / speed))

        for i in range(len(progresses)):
            progresses[i] += speeds[i] * days

        while len(progresses) > 0:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
                continue
            break

        answer.append(count)

    return answer

def solution1(progresses, speeds):
    answer = []
    all_days = 0
    while len(progresses) > 0:

        progress = progresses.pop(0)
        speed = speeds.pop(0)
        count = 1

        days = math.ceil(((100 - progress - (all_days * speed)) / speed))
        all_days += days

        while len(progresses) > 0:
            if progresses[0] + (all_days * speeds[0]) >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
                continue
            break

        answer.append(count)

    return answer


# print(solution([1, 30], [99, 69]))
print(solution([97, 97], [2, 2]))
# print(solution([2, 2, 1, 2], [1, 1, 1, 1]))
# print(solution([99, 98, 97, 96], [1, 1, 1, 1]))
