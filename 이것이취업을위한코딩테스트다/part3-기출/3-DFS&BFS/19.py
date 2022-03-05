import sys
from copy import deepcopy

input = sys.stdin.readline

def min_calculation(index, operation, calculation_result, add, sub, mul, div):
    if index == N:
        return calculation_result

    if operation == 0:
        calculation_result += num_list[index]
        add -= 1
    elif operation == 1:
        calculation_result -= num_list[index]
        sub -= 1
    elif operation == 2:
        calculation_result *= num_list[index]
        mul -= 1
    elif operation == 3:
        if calculation_result < 0:
            calculation_result = -1 * (abs(calculation_result) // num_list[index])
        else:
            calculation_result //= num_list[index]
        div -= 1

    if (add + sub + mul + div) == 0:
        return calculation_result

    result = []
    for i in range(4):
        result = []
        # 언제 값들을 복사할지! 주의하자!
        # 리스트, 딕셔너리와 같은 뎁스가 있는 데이터가 아니면 카피를 할 필요가 없다.
        # 이 문제의 경우 new_operation_count 의 경우도 길이가 4이고 각각이 더하기, 빼기, 곱하기, 나누기를 의미하는 것이 결정되어있으므로
        # add, sub, mul, div 라는 네 변수로 표현한다면 copy 를 할 필요성이 사라진다.
        # new_index = index + 1
        # new_calculation_result = calculation_result
        # new_operation_count = deepcopy(operation_count)
        # print(new_index, new_calculation_result, new_operation_count)
        # if new_operation_count[i] != 0:
        #     result.append(min_calculation(index + 1, i, calculation_result, new_operation_count))

    # print(result)
    return min(result)


def max_calculation(index, operation, calculation_result, operation_count):
    if index == N:
        return calculation_result

    if operation == 0:
        calculation_result += num_list[index]
        operation_count[0] -= 1
    elif operation == 1:
        calculation_result -= num_list[index]
        operation_count[1] -= 1
    elif operation == 2:
        calculation_result *= num_list[index]
        operation_count[2] -= 1
    elif operation == 3:
        if calculation_result < 0:
            calculation_result = -1 * (abs(calculation_result) // num_list[index])
        else:
            calculation_result //= num_list[index]
        operation_count[3] -= 1

    if sum(operation_count) == 0:
        return calculation_result

    result = []
    for i in range(4):
        # new_index = index + 1
        # new_calculation_result = calculation_result
        new_operation_count = deepcopy(operation_count)
        # print(new_index, new_calculation_result, new_operation_count)
        if new_operation_count[i] != 0:
            result.append(max_calculation(index + 1, i, calculation_result, new_operation_count))

    # print(result)
    return max(result)


N = int(input())
num_list = list(map(int, input().split()))
operation_list = list(map(int, input().split()))
[add, sub, mul, div] = operation_list

answer = num_list[0]

print(max_calculation(0, -1, answer, operation_list))
print(min_calculation(0, -1, answer, operation_list, add, sub, mul, div))


