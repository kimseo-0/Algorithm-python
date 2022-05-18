# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    dic = {}
    for clothe in clothes:
        if clothe[1] in dic:
            dic[clothe[1]] += 1
        else:
            dic[clothe[1]] = 1

    answer = 1
    for num in dic.values():
        answer *= (num + 1)
    answer -= 1

    print(answer)
    return answer


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])