# 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = [int(number[0])]
    for i in range(1, len(number)):
        if k == 0:
            answer.append(int(number[i]))
            continue

        while len(answer) > 0:
            if k == 0:
                break
            if answer[-1] >= int(number[i]):
                break

            answer.pop()
            k -= 1

        answer.append(int(number[i]))

    for i in range(k):
        answer.pop()

    return "".join(map(str, answer))


solution("1924", 2)
