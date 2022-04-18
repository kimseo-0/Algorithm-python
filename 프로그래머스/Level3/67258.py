# 2020 카카오 인턴십 > 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    count = len(set(gems))
    min_range = len(gems)

    start = 0
    end = len(gems) - 1

    answer = [start, end]

    while end > start:
        mid = (start + end) // 2

    answer = [x + 1 for x in answer]
    print(answer)
    return answer


solution(["AA", "AB", "AC", "AA", "AC"])
