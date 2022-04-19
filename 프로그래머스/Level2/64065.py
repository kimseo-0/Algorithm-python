# 2019 카카오 개발자 겨울 인턴십 > 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    set_list = list(map(lambda x: list(map(int, x.split(","))), s[2:len(s) - 2].split("},{")))
    print(set_list)

    set_list.sort(key=lambda x: len(x))

    for i in range(len(set_list)):
        for j in range(len(set_list[i])):
            if set_list[i][j] not in answer:
                answer.append(set_list[i][j])
                break
    print(answer)
    return answer


solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
# solution("{{1,2,3}}")
