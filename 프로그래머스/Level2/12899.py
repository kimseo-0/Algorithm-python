# 연습문제 > 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''
    while True:
        rest = n % 3
        n = n // 3

        if rest == 1:
            answer = '1' + answer
        elif rest == 2:
            answer = '2' + answer
        else:
            n -= 1
            answer = '4' + answer

        if n == 0:
            break

    return answer

def solution1(n):
    answer = ''
    while True:
        rest = n % 3
        n = n // 3

        if rest == 0:
            answer = '1' + answer
        elif rest == 1:
            answer = '2' + answer
        else:
            n -= 1
            answer = '4' + answer

        if n == 0:
            break

    return answer

def solution2(n):
    answer = ''
    li = ['1', '2', '4']
    while n > 0:
        n -= 1
        rest = n % 3
        n = n // 3
        answer = li[rest] + answer

    return answer


print(solution(1))  # n = 0 rest = 1
print(solution(2))  # n = 0 rest = 2
print(solution(3))  # n = 0 rest = 0

print(solution1(1))  # n = 0 rest = 0
print(solution1(2))  # n = 0 rest = 1
print(solution1(3))  # n = 0 rest = 2
