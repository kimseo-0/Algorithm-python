# https://programmers.co.kr/learn/courses/30/lessons/62048
# 멀쩡한 사각형
# 

import math

def solution(w, h):
    answer = 0

    if w < h:
        start = 0
        for i in range(w):
            end = (h * (i + 1)) / w
            answer += math.ceil(end) - int(start)
            start = end
    elif w > h:
        start = 0
        for i in range(h):
            end = (w * (i + 1)) / h
            answer += math.ceil(end) - int(start)
            start = end
    else:
        answer = w

    return w * h - answer


print(solution(8, 12))
