# 2019 카카오 개발자 겨울 인턴십 > 불량 사용자
# https://programmers.co.kr/learn/courses/30/lessons/64064

from copy import deepcopy


def check(b_id, u_id):
    if len(b_id) != len(u_id):
        return False
    for i in range(len(b_id)):
        if b_id[i] == '*':
            continue
        if b_id[i] != u_id[i]:
            return False
    return True

def solution(user_id, banned_id):
    ban_candidate_list = [[]]

    for b_id in banned_id:
        ban_id_list = []
        for u_id in user_id:
            if check(b_id, u_id):
                ban_id_list.append(u_id)

        new_ban_candidate_list = []
        for i in range(len(ban_candidate_list)):
            for ban_id in ban_id_list:
                new_ban_candidate = deepcopy(ban_candidate_list[i])

                if ban_id not in new_ban_candidate:
                    new_ban_candidate.append(ban_id)
                    new_ban_candidate_list.append(sorted(new_ban_candidate))

        ban_candidate_list = deepcopy(new_ban_candidate_list)

    answer_list = set(tuple(item) for item in ban_candidate_list)
    # print(answer_list)

    return len(answer_list)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
# print(solution(["11", "22", "33", "44", "55", "66", "77", "88"], ["**", "**", "**", "**", "**", "**", "**", "**"]))

# [[]]
# [[frodo], [fradi]] < [frodo, fradi]
# [[frodo, crodo], [fradi, crodo], [fradi, frodo]] < [frodo, crodo]
