# 괄호 변환

import sys
input = sys.stdin.readline

def check_balance_index(p):
    left = 0
    right = 0
    good = True
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        else:
            right += 1
        if right > left:
            good = False
        if left == right:
            return i, good

def solution(p):
    result = ''

    if p == "":
        return result

    index, good_bracket = check_balance_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    v = solution(v)

    if good_bracket:
        return u + v
    else:
        result = "(" + v + ")"
        for i in range(1, len(u) - 1):
            if u[i] == ")":
                result += "("
            else:
                result += ")"

    return result


print('"' + solution("()") + '"')
