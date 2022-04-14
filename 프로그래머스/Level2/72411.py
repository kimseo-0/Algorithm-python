# 메뉴 리뉴얼
from itertools import combinations


def solution(orders, course):
    answer = []

    for t in course:
        combination_list = []
        for order in orders:
            combination_list.append(list(combinations(sorted(order), t)))
        # print(combination_list)

        t_answer = []
        max_count = 2
        for i in range(len(orders)):
            for j in range(len(combination_list[i])):
                count = 0
                for k in range(i, len(orders)):
                    if combination_list[i][j] in combination_list[k]:
                        # combination_list[k].remove(combination_list[i][j])
                        count += 1

                if count > max_count:
                    max_count = count
                    t_answer = [combination_list[i][j]]
                elif count == max_count:
                    t_answer.append(combination_list[i][j])
                # print(max_count, t_answer)
        answer.extend(t_answer)
    answer = list(map(lambda x: ''.join(s for s in x), answer))
    answer.sort()
    print(answer)
    return answer


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
