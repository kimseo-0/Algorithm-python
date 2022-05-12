# 예산 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985
import math

def solution(n, a, b):
    answer = 0

    while 1:
        answer += 1
        if (b - a == 1 and a % 2 == 1) or (a - b == 1 and b % 2 == 1):
            break
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)

    print(answer)
    return answer


solution(8, 2, 3)

# a 가 반드시 b 보다 작다는 조건은 없었다.
# 조건은 더 잘 확인 할 것
