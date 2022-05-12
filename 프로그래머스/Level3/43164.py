from copy import deepcopy


def DFS(dic, start, count, answer):
    # print(answer)
    if count == 0:
        return answer

    if start in dic:
        for end in dic[start]:
            new_dic = deepcopy(dic)
            new_dic[start].remove(end)
            new_answer = DFS(new_dic, end, count - 1, [*answer, end])
            if new_answer:
                return new_answer
    else:
        return False

    return False

def solution(tickets):
    answer = []
    dic = {}

    count = len(tickets)

    tickets.sort()

    for ticket in tickets:
        if ticket[0] in dic:
            dic[ticket[0]].append(ticket[1])
        else:
            dic[ticket[0]] = [ticket[1]]

    start = "ICN"
    answer.append(start)
    answer = DFS(dic, start, count, answer)

    print(answer)
    return answer


# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["ATL", "ABC"], ["SFO", "ICN"]])


#  참고용
from collections import defaultdict

def solution_other(tickets):
    r = defaultdict(list)
    for i, j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()

    s = ["ICN"]
    p = []
    while s:
        q = s[-1]
        if r[q]:
            s.append(r[q].pop(0))
        else:
            p.append(s.pop())
    return p[::-1]
