# # 2020 카카오 인턴십 > 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations


def DFS(expression_list, ops, index):
    if index > 3 or (expression_list[0].isnumeric() and len(expression_list) <= 1):
        return int(expression_list[0])

    result = 0
    for i in range(len(expression_list)):
        expression_list[i] = expression_list[i].split(ops[index])
        next_result = DFS(expression_list[i], ops, index + 1)

        if i == 0:
            result += next_result
        else:
            if ops[index - 1] == '+':
                result += next_result
            elif ops[index - 1] == '-':
                result -= next_result
            elif ops[index - 1] == '*':
                result *= next_result

    return result


def solution(expression):
    answer = 0
    operations = ['+', '*', '-']  # + - *, + * -, - * +, * + -
    permutation_list = list(permutations(operations))

    for ops in permutation_list:
        ops = list(ops)
        ops.append(" ")
        result = abs(DFS([expression], ops, 0))
        answer = max(answer, result)
    return answer


# solution("100-200*300-500+20")
# solution("50*6-3*2")
solution("3*6*3")
